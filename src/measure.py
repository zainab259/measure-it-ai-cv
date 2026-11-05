import argparse
import json
import os

import cv2
import numpy as np
import torch
import segmentation_models_pytorch as smp


def load_model(checkpoint_path, device):
    model = smp.Unet(
        encoder_name="mobilenet_v2",
        encoder_weights=None,
        in_channels=3,
        classes=1,
        activation=None,
    ).to(device)

    checkpoint = torch.load(
        checkpoint_path,
        map_location=device,
        weights_only=False,
    )

    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    return model


def segment_object(model, image, device):
    height, width = image.shape[:2]

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(rgb, (256, 256))

    tensor = torch.from_numpy(
        resized.astype(np.float32) / 255.0
    ).permute(2, 0, 1)

    mean = torch.tensor(
        [0.485, 0.456, 0.406]
    ).view(3, 1, 1)

    std = torch.tensor(
        [0.229, 0.224, 0.225]
    ).view(3, 1, 1)

    tensor = ((tensor - mean) / std)
    tensor = tensor.unsqueeze(0).to(device)

    with torch.no_grad():
        probability = torch.sigmoid(
            model(tensor)
        )[0, 0].cpu().numpy()

    probability = cv2.resize(
        probability,
        (width, height),
        interpolation=cv2.INTER_LINEAR,
    )

    mask = (probability >= 0.5).astype(np.uint8)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    bright = cv2.inRange(
        hsv,
        (0, 0, 145),
        (179, 110, 255),
    )

    refined = (
        mask * (bright > 0).astype(np.uint8)
    )

    refined = cv2.morphologyEx(
        refined,
        cv2.MORPH_CLOSE,
        np.ones((9, 9), np.uint8),
    )

    contours, _ = cv2.findContours(
        refined,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    if not contours:
        return None

    contour = max(contours, key=cv2.contourArea)

    area_fraction = (
        cv2.contourArea(contour) / (width * height)
    )

    if area_fraction < 0.01:
        return None

    rect = cv2.minAreaRect(contour)

    _, (rw, rh), _ = rect

    points = cv2.boxPoints(rect).astype(np.int32)

    # Foreground probability is an uncalibrated proxy.
    foreground = refined.astype(bool)

    confidence_proxy = (
        float(probability[foreground].mean())
        if foreground.any()
        else 0.0
    )

    return {
        "length_px": float(max(rw, rh)),
        "width_px": float(min(rw, rh)),
        "confidence_proxy": confidence_proxy,
        "area_fraction": float(area_fraction),
        "points": points,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Measure-It medicine-box measurement"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Input image path",
    )

    parser.add_argument(
        "--model",
        default=(
            "/content/drive/MyDrive/MeasureIt/models/"
            "best_unet_mobilenetv2.pth"
        ),
    )

    parser.add_argument(
        "--reference-px",
        type=float,
        default=None,
        help="Verified pixel distance between reference marks",
    )

    parser.add_argument(
        "--reference-mm",
        type=float,
        default=None,
        help="Known physical distance between those marks",
    )

    parser.add_argument(
        "--output-dir",
        default="measurement_output",
    )

    parser.add_argument(
        "--calibration",
        default=None,
        help="Optional OpenCV camera_calibration.npz",
    )

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    result = {
        "image": args.image,
        "status": "REFUSED",
    }

    image = cv2.imread(args.image)

    if image is not None and args.calibration:

        calibration = np.load(args.calibration)

        K = calibration["camera_matrix"]
        dist = calibration["dist_coeffs"]

        h, w = image.shape[:2]

        expected_w = int(calibration["image_width"])
        expected_h = int(calibration["image_height"])

        if (w, h) != (expected_w, expected_h):
            raise ValueError(
                "REFUSED: Calibration resolution mismatch. "
                "Use a compatible image or recalibrate the camera."
            )

        else:
            image = cv2.undistort(image, K, dist)
            result["undistortion"] = "applied"

    if image is None:
        result["reason"] = "Invalid or missing image"

    elif not os.path.isfile(args.model):
        result["reason"] = "Model checkpoint unavailable"

    else:
        device = torch.device("cpu")
        model = load_model(args.model, device)

        detection = segment_object(
            model,
            image,
            device,
        )

        if detection is None:
            result["reason"] = "Medicine box not detected"

        else:
            length_px = detection["length_px"]
            width_px = detection["width_px"]

            result["length_px"] = round(length_px, 2)
            result["width_px"] = round(width_px, 2)
            result["confidence_proxy"] = round(
                detection["confidence_proxy"], 4
            )

            # Conservative experimental threshold.
            # Not statistically calibrated.
            if detection["confidence_proxy"] < 0.70:
                result["reason"] = (
                    "Low foreground probability"
                )

            elif (
                args.reference_px is None
                or args.reference_mm is None
            ):
                result["reason"] = (
                    "Reference scale unavailable"
                )

            elif (
                not np.isfinite(args.reference_px)
                or not np.isfinite(args.reference_mm)
                or args.reference_px <= 0
                or args.reference_mm <= 0
            ):
                result["reason"] = (
                    "Invalid reference dimensions"
                )

            else:
                pixels_per_mm = (
                    args.reference_px / args.reference_mm
                )

                result["status"] = "MEASURED"
                result["length_mm"] = round(
                    length_px / pixels_per_mm, 2
                )
                result["width_mm"] = round(
                    width_px / pixels_per_mm, 2
                )
                result["reference_method"] = (
                    "manual_verified_pixel_distance"
                )
                result["pixels_per_mm"] = round(
                    pixels_per_mm, 5
                )

            overlay = image.copy()

            cv2.drawContours(
                overlay,
                [detection["points"]],
                0,
                (0, 255, 0),
                3,
            )

            label = (
                f"{result['length_mm']:.1f} x "
                f"{result['width_mm']:.1f} mm"
                if result["status"] == "MEASURED"
                else "MEASUREMENT REFUSED"
            )

            cv2.putText(
                overlay,
                label,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0)
                if result["status"] == "MEASURED"
                else (0, 0, 255),
                2,
            )

            cv2.imwrite(
                os.path.join(
                    args.output_dir,
                    "measurement_overlay.png",
                ),
                overlay,
            )

    with open(
        os.path.join(
            args.output_dir,
            "measurement_result.json",
        ),
        "w",
    ) as file:
        json.dump(result, file, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
