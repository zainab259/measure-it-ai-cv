# Measure It — Objectives

## Project Overview

Object: Rectangular matchbox

Goal: Develop a computer vision system that
segments a matchbox and estimates its real
width and height in millimetres.

## MO-1: Measurement Accuracy

### What is measured?
The absolute difference between the actual
matchbox dimensions and the AI-predicted
dimensions, measured in millimetres.

### How is it measured?
Measure at least 10 instances using a physical
ruler or calliper.

Compare the ground-truth width and height
with the system's predicted measurements.

Calculate:
- Absolute Error (mm)
- Percentage Error (%)
- Mean Absolute Error (MAE)
- Median Absolute Error
- Maximum Absolute Error

### Target
Mean Absolute Error <= 3 mm for both
width and height.

### Conditions
- Same mobile phone camera.
- Fixed camera zoom and resolution.
- Calibrated camera.
- Matchbox and reference on the same flat plane.
- Reference object fully visible.
- Adequate lighting.

### Not Included
- Partially hidden objects.
- Severely blurred images.
- Images without a detectable reference object.

### Results
Pending implementation and testing.

## MO-2: Segmentation Accuracy

### What is measured?
The overlap between the predicted matchbox
segmentation mask and the manually labelled mask.

### How is it measured?
Evaluate the trained U-Net model on the
fixed, unseen test dataset.

Report:
- Mask IoU
- mAP@0.5
- mAP@0.5:0.95
- Precision
- Recall

### Target
Mean mask IoU >= 0.75 on the test split.

### Conditions
- Original matchbox photographs.
- Fixed 70/20/10 dataset split.
- Test images excluded from training and tuning.
- Same preprocessing during evaluation.

### Not Included
- Objects other than the selected matchbox.
- Images not included in the fixed test set.

### Results
Pending model training and evaluation.

## Camera Calibration

Report:
- Number of calibration images.
- Number of successfully detected checkerboards.
- Camera matrix.
- Distortion coefficients.
- Reprojection error.

Results: Pending calibration.

## Hardware and Software

Training environment: Google Colab CPU

Record the following during implementation:
- CPU model
- RAM
- Operating system
- Python version
- PyTorch version
- OpenCV version
- Mobile phone camera model
- Original photograph resolution

## Evidence

All reported results will come from actual
program output.

Training metrics, measurement tables and
calibration results will be added after testing.

Targets will not be changed merely to match
the achieved results.

## Final Status

Not yet evaluated.
