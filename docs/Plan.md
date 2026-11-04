## Plan Revision — 4 November 2026

Originally, a matchbox was selected as the target object.

The object was changed to a rectangular D-Tres Vitamin D3
medicine box because a matchbox was not available.

The medicine box has a flat rectangular surface and
clear boundaries suitable for segmentation and measurement.

This change does not affect the selected segmentation
architecture or the overall measurement workflow.
# Measure It — Project Plan

## Objective
Build a computer vision system that measures the width and height of a rectangular D-Tres Vitamin D3 medicine box in millimetres.

## Approach
1. Calibrate a mobile phone camera using OpenCV
   and at least 20 checkerboard photographs.
2. Capture at least 70 original matchbox images.
3. Undistort images using saved calibration parameters.
4. Annotate the matchbox with segmentation masks.
5. Create a fixed 70/20/10 train/validation/test split.
6. Fine-tune a lightweight U-Net segmentation model.
7. Evaluate segmentation performance on unseen test images.
8. Detect a reference object of known dimensions.
9. Convert pixel measurements into millimetres.
10. Compare predictions with physical measurements.

## Time Budget
- Planning and Git setup: 0.5 hours
- Camera calibration: 1 hour
- Dataset collection and annotation: 2 hours
- Training preparation: 1 hour
- Measurement pipeline: 1.5 hours
- Evaluation: 1 hour
- Documentation and recording: 1 hour

Total active work: 8 hours.

## Technology
- Python
- OpenCV
- PyTorch
- U-Net with MobileNetV2 encoder
- Google Colab (CPU)
- GitHub

## Initial Scope
Prioritise camera calibration, dataset creation,
segmentation training, and image-to-mm inference.

Advanced failure-condition testing will be attempted
only after the core pipeline works.

## Reproducibility
Fix the random seed, preserve dataset split files,
record library versions, and save calibration parameters.

## Limitations
Screen-based checkerboard calibration is being tested
because a printed board is not currently available.
Its reliability must be verified before use.
