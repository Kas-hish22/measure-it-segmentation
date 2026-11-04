# Project Objectives

## MO-1: Measurement Accuracy

- What is measured: Absolute error in ATM-card width and height measurements.
- How: Compare system measurements with independently measured ground-truth dimensions for at least 10 test instances.
- Initial target: Mean absolute error (MAE) no greater than 2.0 mm.
- Conditions: Fixed camera settings, card and reference marker on the same plane, controlled lighting.
- Exclusions: Partially hidden cards and images where the reference marker cannot be detected.

## MO-2: Inference Speed

- What is measured: Time taken by the inference pipeline to process one image.
- How: Run the pipeline five times on the same hardware and report median and spread.
- Initial target: Median processing time no greater than 2 seconds per image.
- Conditions: Record the Colab hardware and image resolution.
