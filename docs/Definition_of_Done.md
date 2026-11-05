# Measure It — Definition of Done

This checklist tracks assessment requirements. A task is marked complete only when supporting evidence is available.

## 1. Camera Calibration

- [x] Capture at least 20 checkerboard photographs.
  - Evidence: 26 photographs collected.
- [x] Detect checkerboard corners using OpenCV.
  - Evidence: 25 successful detections.
- [x] Calculate camera matrix and distortion coefficients.
  - Evidence: Calibration notebook output.
- [x] Report reprojection error.
  - Evidence: RMS error = 0.519 pixels.
- [x] Save calibration parameters.
  - Evidence: `camera_calibration.npz` saved in Google Drive.
- [ ] Verify reliable undistortion and calibration compatibility for measurement images.
- [ ] Include calibration code, images, and parameters in the final repository.

## 2. Dataset Collection

- [x] Select a physical object.
  - Evidence: D-Tres Vitamin D3 medicine box.
- [x] Collect at least 70 photographs.
  - Evidence: 70 candidate images collected by the candidate.
- [x] Check image dimensions and exact duplicates.
  - Evidence: 70 images, zero exact duplicate groups.
- [x] Generate fixed train/validation/test filename lists.
  - Evidence: 49 training, 14 validation, 7 testing.
- [x] Commit split lists before model training.
  - Evidence: `dataset/splits/` on `dev-test01`.
- [ ] Verify and save undistorted dataset images.
- [ ] Generate and verify 70 segmentation masks.
- [ ] Commit the required images, annotations, and dataset metadata.

## 3. Segmentation Model

- [ ] Implement U-Net with MobileNetV2 encoder.
- [ ] Train or fine-tune using original dataset images.
- [ ] Use training data only for parameter updates.
- [ ] Select the best checkpoint using validation data.
- [ ] Evaluate on the untouched test dataset.
- [ ] Report mask IoU.
- [ ] Report mAP@0.5.
- [ ] Report mAP@0.5:0.95.
- [ ] Report precision and recall.
- [ ] Save model weights and training configuration.

## 4. Image-to-Millimetres Pipeline

- [ ] Accept a new image through one command.
- [ ] Apply camera undistortion.
- [ ] Predict the medicine-box segmentation mask.
- [ ] Detect a reference object of known dimensions.
- [ ] Convert pixel dimensions into millimetres.
- [ ] Report width, height, and confidence.
- [ ] Generate a segmentation overlay.
- [ ] Handle object-not-found cases.
- [ ] Handle reference-not-found cases.

## 5. Physical Accuracy Evaluation

- [ ] Measure at least 10 instances physically.
- [ ] Compare physical measurements with predictions.
- [ ] Report a per-instance accuracy table.
- [ ] Calculate mean absolute error in millimetres.
- [ ] Calculate percentage error.
- [ ] Report median and maximum errors.
- [ ] Compare raw and undistorted measurements.

## 6. Additional Evaluation

- [ ] Evaluate MO-1: Measurement accuracy.
- [ ] Evaluate MO-2: Segmentation accuracy.
- [ ] Measure one performance or accuracy target.
- [ ] Investigate one failure condition.
- [ ] Implement unreliable-measurement rejection.
- [ ] Report refusal threshold and refused-image count.

## 7. GitHub and Documentation

- [x] Create a public GitHub repository.
  - Evidence: `zainab259/measure-it-ai-cv`
- [x] Create the required development branch.
  - Evidence: `dev-test01`
- [x] Create the Project Plan.
  - Evidence: `docs/Plan.md`
- [x] Create the Objectives document.
  - Evidence: `docs/Objectives.md`
- [x] Create the Definition of Done.
  - Evidence: This document.
- [x] Record the target-object change.
  - Evidence: Plan revision.
- [ ] Commit calibration and dataset implementation.
- [ ] Commit training and evaluation implementation.
- [ ] Document software versions and hardware.
- [ ] Create complete
