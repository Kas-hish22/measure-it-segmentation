# Measure It — Final Project Report

Date: 4 November 2026

## 1. Project Objective
Develop a computer-vision prototype to segment an ATM/debit card and estimate its dimensions.

## 2. Dataset
- Total images: 100
- Training: 70
- Validation: 20
- Testing: 10
- Image resolution: 3048 x 4064 pixels
- Segmentation masks generated using SAM 2.1.

Note: These masks are automatically generated pseudo-labels, not manually verified ground truth.

## 3. Camera Calibration
- Checkerboard inner corners: 9 x 6
- Square size: 20 mm
- Calibration images captured: 23
- Successful detections: 13
- RMS reprojection error: 1.2078 pixels

The checkerboard was displayed on a screen rather than printed. This is a preliminary calibration and requires independent validation.

## 4. Model
- Architecture: Mask R-CNN with ResNet-50 FPN
- Pretrained COCO weights
- Framework: PyTorch / Torchvision
- GPU: NVIDIA Tesla T4
- Training epochs: 8
- Best epoch: 4
- Best validation loss: 0.2419
- Final training loss: 0.0868

## 5. Test Results
- Test images: 10
- Mean IoU against SAM-generated masks: 0.9722
- Mean Dice against SAM-generated masks: 0.9859

These metrics measure agreement with automatically generated pseudo-labels, not independently verified segmentation accuracy.

## 6. Preliminary Dimension Estimate
Nominal ID-1 card reference dimensions:
- Width: 85.60 mm
- Height: 53.98 mm
- Reference aspect ratio: approximately 1.586

A strict 5.5% aspect-ratio filter selected 1 out of 100 images.
For this selected image, the preliminary estimated dimensions were:
- Width: 85.60 mm (assumed reference)
- Height: 53.99 mm (derived estimate)

This is not an independent physical measurement. The other 99 images were excluded from this strict measurement subset.

## 7. Limitations
- SAM-generated masks were not manually verified.
- Screen-based checkerboard calibration has scale and geometry limitations.
- No independent reference marker or physical measurement was available in the captured card images.
- The nominal card dimensions were assumed rather than independently measured.
- The test metrics are calculated against pseudo-labels.

## 8. Conclusion
The project demonstrates a working image segmentation pipeline using SAM-generated annotations and a fine-tuned Mask R-CNN model. Preliminary card dimension estimation was demonstrated using a nominal card-size reference.

Further work is required to validate camera calibration, segmentation masks, and millimetre measurements against independent physical references.