# Measure It — Objectives

## Project Overview

**Target Object:** D-Tres Vitamin D3 medicine box

**Goal:** Develop a computer vision system that segments the medicine box's rectangular front face and estimates its physical width and height in millimetres.

**Environment:** Python, OpenCV, PyTorch, U-Net, Google Colab CPU.

## MO-1 — Measurement Accuracy

**What is measured:** Absolute difference between actual and predicted medicine-box dimensions, in millimetres.

**Method:**

1. Measure the physical dimensions using a ruler or calliper.
2. Capture at least 10 measurement instances with a known-size reference object in the same plane.
3. Run the measurement pipeline on each image.
4. Calculate width error, height error, and percentage error.
5. Report mean, median, and worst-case errors.

**Target:** Mean absolute error of 3 mm or less for both width and height.

**Conditions:** Same calibrated camera, stable zoom and focus, adequate lighting, visible reference, and approximately front-facing measurement plane.

**Excluded Conditions:** Severely blurred images, occluded reference objects, and images where reliable measurement is impossible. Refusals must be recorded.

**Justification:** A tolerance of 3 mm is an initial practical target for the small rectangular packaging. Its suitability will be evaluated against the object's actual size.

**Results:** Pending physical measurements and system evaluation.

## MO-2 — Segmentation Accuracy

**What is measured:** Agreement between predicted masks and verified ground-truth masks.

**Method:**

1. Prepare segmentation masks using OpenCV-assisted annotation.
2. Inspect and correct inaccurate masks.
3. Train U-Net using the fixed training split.
4. Select checkpoints using validation data only.
5. Evaluate once on the untouched test set.

**Metrics:**

- Mask IoU
- mAP@0.5
- mAP@0.5:0.95
- Precision
- Recall

**Target:** Mean mask IoU of at least 0.75 on the fixed test dataset.

**Conditions:** Same object, fixed dataset split, consistent preprocessing, and verified segmentation masks.

**Excluded Conditions:** Other object classes and images outside the declared evaluation dataset.

**Results:** Pending model training.

## Camera Calibration

**Method:** OpenCV checkerboard calibration.

**Recorded preliminary results:**

- Calibration photographs: 26
- Successful corner detections: 25
- Image resolution: 1600 × 720
- RMS reprojection error: 0.519 pixels
- Mean per-image RMS error: 0.384 pixels
- Worst per-image RMS error: 1.290 pixels

**Status:** Provisional. Calibration was performed using a laptop-displayed checkerboard and WhatsApp-transferred photographs. Physical measurement reliability remains unverified.

## Dataset

- Object
