# Measure It — Segmentation and Metric Measurement

A computer vision project for card segmentation and approximate dimensional measurement using camera calibration and Mask R-CNN.

## Project Structure

- docs/ — Project documentation and reports.
- dataset/splits/split.csv — Fixed 70/20/10 dataset split.
- artifacts/calibration/ — Camera calibration parameters.
- artifacts/models/ — Trained model checkpoint.
- artifacts/ — Evaluation and measurement results.
- inference/ — Image inference script.

## Model

Fine-tuned torchvision Mask R-CNN ResNet50-FPN.
Training used 100 card images with SAM 2.1-generated pseudo-labels.

## Installation

Run: pip install -r requirements.txt

## Run Inference

python inference/measure.py --image path/to/image.jpg --reference-width-mm 85.60 --reference-width-px PIXELS

The reference width in pixels must be measured manually from the same undistorted image.

## Limitations

Reference-object detection is manual, not automatic. Independent calliper validation has not been completed. Segmentation metrics are evaluated against SAM pseudo-labels, not independently verified ground truth.
