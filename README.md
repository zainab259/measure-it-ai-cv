# Measure-It AI


## Implementation and Reproduction

### Dataset
70 images, 70 masks, fixed 49/14/7 split.

### Model
U-Net with MobileNetV2 encoder.
Checkpoint: models/best_unet_mobilenetv2.pth
### Trained Model Checkpoint

- Architecture: U-Net
- Encoder: MobileNetV2
- Pretrained encoder weights: ImageNet
- Checkpoint: `models/best_unet_mobilenetv2.pth`
**SHA-256:**
`f23b88196bca133541db2f630b5770b34c381c626a9766bc8d59ccc9df946b0e`

### Installation
Run: pip install -r requirements.txt

### Measurement command
Run:

python src/measure.py --image photo.jpeg --model models/best_unet_mobilenetv2.pth

Without a verified reference, millimetre measurement
is refused.

With a manually established reference:

python src/measure.py --image photo.jpeg --model models/best_unet_mobilenetv2.pth --reference-px 420 --reference-mm 60

The example reference coordinates are illustrative,
not automatically detected.

### Calibration
Optional argument:
--calibration calibration/camera_calibration.npz

Calibration requires compatible image resolution.

### Results
See results/ for test metrics and measurement outputs.

### Known limitations
- Automatic reference detection is incomplete.
- Nine additional physical comparisons are pending.
- Full undistortion measurement-error comparison is pending.
- Confidence thresholds are experimental.

See docs/Decision_Record.md.
