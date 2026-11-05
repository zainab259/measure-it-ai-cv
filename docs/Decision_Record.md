
# Measure-It Decision Record

## Object
D-Tres medicine box.

## Calibration
25 usable checkerboard photographs.
OpenCV RMS reprojection error: 0.519 pixels.
Calibration is provisional because the checkerboard
was displayed on a laptop screen.

## Dataset
70 original images and 70 CVAT segmentation masks.
Train/validation/test split: 49/14/7.

## Model
U-Net with MobileNetV2 encoder.
ImageNet pretrained encoder weights.

## Segmentation results
Validation IoU: 0.8158.
Test IoU: 0.8749.
Pixel precision: 0.9175.
Pixel recall: 0.9528.

Single-class AP uses a simplified one-object
evaluation method, not standard COCO detector AP.

## Measurement
Prototype accepts a manually verified reference scale.
First preliminary measurement:
Actual: 86.36 x 63.50 mm.
Estimated: 93.14 x 70.14 mm.
Preliminary MAE: 6.71 mm.

## Failure handling
Refuses measurement for missing object, missing or
invalid reference, and incompatible requested calibration.

## Limitations
Automatic reference detection is incomplete.
Only one preliminary physical comparison is complete.
Raw-versus-undistorted millimetre-error validation
is incomplete.
Confidence scores are not statistically calibrated.
