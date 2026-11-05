# Measure It — Project Plan

## Objective
Build a computer vision system that detects a rectangular D-Tres Vitamin D3 medicine box and measures the width and height of its front face in millimetres using camera calibration, image segmentation, and a reference object of known physical dimensions.

## Implementation Approach

1. **Camera Calibration:** Capture at least 20 checkerboard images using a mobile phone camera. Calculate the camera matrix, distortion coefficients, and reprojection error using OpenCV.
2. **Dataset Collection:** Capture at least 70 photographs of the D-Tres medicine box using the same camera. Preserve the images and record their resolutions.
3. **Image Undistortion:** Apply the saved calibration parameters, accounting for image orientation and resolution.
4. **Dataset Splitting:** Create and commit fixed training (70%), validation (20%), and test (10%) filename lists before model training. Keep detected near-duplicate images within the same split.
5. **Segmentation Annotation:** Use OpenCV-assisted image processing to generate initial segmentation masks. Visually inspect every mask and manually correct inaccurate boundaries.
6. **Model Training:** Fine-tune a lightweight U-Net with a MobileNetV2 encoder using PyTorch on Google Colab CPU.
7. **Model Evaluation:** Evaluate the model on the untouched test split using mask IoU, mAP@0.5, mAP@0.5:0.95, precision, and recall.
8. **Metric Measurement:** Detect a reference object of known dimensions, convert pixel measurements into millimetres, and report width, height, and confidence.
9. **Accuracy Verification:** Compare system predictions with physical measurements for at least 10 instances. Report measurement errors and compare raw versus undistorted images.
10. **Submission:** Finalize documentation, evidence, README, model weights, Git commits, pull request, and a Loom recording of no more than five minutes.

## Time Budget

| Activity | Active Work |
|---|---:|
| Planning and Git setup | 0.5 hours |
| Camera calibration | 1 hour |
| Dataset collection and annotation | 2 hours |
| Training preparation | 1 hour |
| Measurement pipeline | 1.5 hours |
| Evaluation | 1 hour |
| Documentation and recording | 1 hour |
| **Total** | **8 hours** |

Model training and dependency-installation waiting time are excluded from the active-work budget, as permitted by the assessment.

## Technology

- Python, OpenCV, NumPy
- PyTorch and U-Net (MobileNetV2 encoder)
- Google Colab (CPU)
- CVAT for initial annotation experiments
- OpenCV-assisted mask generation
- Git and GitHub

## Reproducibility

- Random seed: `42`
- Dataset: 70 original photographs captured by the candidate
- Fixed split: 49 training, 14 validation, 7 testing images
- Preserve committed split filename lists
- Record library versions, hardware, and training configuration
- Save calibration parameters, model checkpoints, and evaluation results
- Never use test images for training, tuning, or checkpoint selection

## Limitations and Risks

- Calibration photographs were captured from a laptop-displayed checkerboard and transferred through WhatsApp.
- Initial calibration used 25 successfully detected checkerboards and produced an RMS reprojection error of approximately 0.519 pixels.
- The calibration remains provisional until its effect on measurement accuracy is verified.
- Dataset images have mixed orientations and resolutions; camera parameters must be applied consistently.
- The candidate must obtain physical measurements of the reference object and medicine box before claiming millimetre accuracy.
- Automatically generated masks may contain boundary errors and require inspection.
- Advanced failure-condition experiments will be attempted after the core pipeline works. Unfinished requirements will be declared honestly.

## Decision Record

### Decision 1 — Target Object

**Originally selected:** Rectangular matchbox.

**Selected approach:** Rectangular D-Tres Vitamin D3 medicine box.

**Reason:** The matchbox was unavailable. The medicine box was physically available and has a clearly defined rectangular front face.

**Trade-off:** The object choice changed, but the segmentation architecture and measurement workflow remain applicable.

### Decision 2 — Annotation Strategy

**Originally selected:** Manually drawing polygons for all 70 images using CVAT.

**Selected approach:** Generate initial masks using OpenCV-assisted image processing in Google Colab, followed by visual inspection and manual correction.

**Reason:** Fully manual annotation would consume a substantial portion of the eight-hour active-work budget.

**Rejected approach and cost:** Manual CVAT annotation offers direct control over boundaries but requires significantly more annotation time.

**Trade-off:** Automated masking is faster but can fail under changing lighting, patterned backgrounds, or unusual object orientations. All generated masks must therefore be checked before training.

**Status:** OpenCV-assisted mask generation is planned; its results have not yet been validated.

## Completion Criteria

Completion will be determined using `docs/Definition_of_Done.md`. Each checked requirement must include supporting evidence. Missed objectives, incomplete features, and limitations will be reported rather than concealed.
