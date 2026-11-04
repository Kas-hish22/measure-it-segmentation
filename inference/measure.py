
import argparse
import cv2
import numpy as np
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--reference-width-mm", type=float, required=True)
    parser.add_argument("--reference-width-px", type=float, required=True)
    parser.add_argument("--confidence", type=float, default=0.5)
    args = parser.parse_args()

    if args.reference_width_mm <= 0 or args.reference_width_px <= 0:
        raise ValueError("Reference dimensions must be positive.")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = maskrcnn_resnet50_fpn(
        weights=None,
        weights_backbone=None,
        num_classes=2
    )

    weights = torch.load(
        "artifacts/models/best_maskrcnn.pth",
        map_location=device,
        weights_only=True
    )
    model.load_state_dict(weights)
    model.to(device)
    model.eval()

    image = cv2.imread(args.image)
    if image is None:
        raise FileNotFoundError(args.image)

    calibration = np.load("artifacts/calibration/camera_calibration.npz")
    undistorted = cv2.undistort(
        image,
        calibration["camera_matrix"],
        calibration["dist_coeffs"]
    )

    rgb = cv2.cvtColor(undistorted, cv2.COLOR_BGR2RGB)
    tensor = torch.from_numpy(rgb.copy()).permute(2, 0, 1).float() / 255.0

    with torch.no_grad():
        prediction = model([tensor.to(device)])[0]

    valid = [
        i for i, score in enumerate(prediction["scores"].cpu().numpy())
        if score >= args.confidence and prediction["labels"][i].item() == 1
    ]

    if not valid:
        print("Object not found. No measurement reported.")
        return

    index = valid[0]
    mask = prediction["masks"][index, 0].cpu().numpy() > 0.5

    contours, _ = cv2.findContours(
        mask.astype(np.uint8),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        print("Object mask is empty. No measurement reported.")
        return

    contour = max(contours, key=cv2.contourArea)
    rect = cv2.minAreaRect(contour)
    width_px, height_px = sorted(rect[1], reverse=True)

    if width_px <= 0 or height_px <= 0:
        print("Invalid mask dimensions.")
        return

    mm_per_pixel = args.reference_width_mm / args.reference_width_px
    width_mm = width_px * mm_per_pixel
    height_mm = height_px * mm_per_pixel

    overlay = undistorted.copy()
    overlay[mask] = (
        0.5 * overlay[mask] + 0.5 * np.array([0, 255, 0])
    ).astype(np.uint8)

    cv2.drawContours(overlay, [contour], -1, (0, 0, 255), 3)
    cv2.imwrite("inference/measurement_overlay.jpg", overlay)

    print(f"Confidence: {prediction['scores'][index].item():.4f}")
    print(f"Width: {width_mm:.2f} mm")
    print(f"Height: {height_mm:.2f} mm")
    print("Overlay: inference/measurement_overlay.jpg")
    print("Scale uses manually supplied reference width.")

if __name__ == "__main__":
    main()
