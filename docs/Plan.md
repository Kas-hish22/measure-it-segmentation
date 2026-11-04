# Measure It — Project Plan

## Goal
Build a camera-calibrated computer vision system that segments an ATM card and measures its width and height in millimetres.

## Object
Standard ATM/debit card. Expected dimensions are 85.60 mm × 53.98 mm. Actual dimensions will be measured independently using a ruler or calliper.

## Approach and Schedule (8 working hours)

1. Initial setup and documentation — 30 minutes.
2. Camera calibration using at least 20 checkerboard images and OpenCV — 60 minutes.
3. Capture and label 100 original card images — 120 minutes.
4. Train and evaluate a Mask R-CNN segmentation model — 150 minutes.
5. Build the calibrated image-to-millimetres inference pipeline — 60 minutes.
6. Validate measurements, compare raw and undistorted images — 60 minutes.
7. Final documentation, reproducibility checks and recording — 40 minutes.

## Technical Approach
- OpenCV for camera calibration and image undistortion.
- A self-captured and manually labelled dataset.
- PyTorch/Torchvision Mask R-CNN, fine-tuned on our own images.
- A measured ArUco reference marker in the same plane as the card.
- Pixel-to-millimetre conversion using the reference marker dimensions.

## Dataset and Evaluation
100 original images, split before training:
70 training, 20 validation and 10 test images.
The test split will not be used for training, tuning or checkpoint selection.

## Initial Scope Decisions
- No Ultralytics YOLO or Roboflow segmentation model.
- No downloaded images of the ATM card.
- Prioritise requirements 1–4 before optional extensions.
- If time is limited, unfinished requirements will be reported honestly.

## Risks
Lighting, reflections, camera tilt, incorrect reference placement and insufficient labelled data may affect measurements.

## Hardware
Google Colab GPU (availability and GPU model to be recorded), local laptop: Intel Core i7, 8 GB RAM. Phone camera model and image resolution to be recorded.

## Decision Record
Chosen: Torchvision Mask R-CNN for instance segmentation.
Rejected: Ultralytics YOLO and Roboflow models because the assessment explicitly prohibits them.
Trade-off: Mask R-CNN training and evaluation may take longer and require more compute.
