import cv2
import numpy as np
from measurements import contour_metrics

class CrackDetector:
    """
    Classical image-processing baseline.
    Finds dark, elongated surface features that may be cracks.
    Lighting, shadows, joints, stains, and surface texture can cause false positives.
    """

    def __init__(self, min_area=30):
        self.min_area = max(1, int(min_area))

    def detect(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Local contrast enhancement helps reveal dark fine features.
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        # Black-hat emphasizes dark features against a lighter background.
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
        blackhat = cv2.morphologyEx(enhanced, cv2.MORPH_BLACKHAT, kernel)

        _, mask = cv2.threshold(
            blackhat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        mask = cv2.morphologyEx(
            mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)
        )

        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        annotated = image.copy()
        detections = []

        for contour in contours:
            area = cv2.contourArea(contour)
            if area < self.min_area:
                continue

            metrics = contour_metrics(contour)
            x, y, w, h = cv2.boundingRect(contour)

            # Shape filter: elongated candidates are more crack-like,
            # but this is only a heuristic and is not a crack classifier.
            if metrics["aspect_ratio"] < 1.5 and area < self.min_area * 3:
                continue

            detections.append({
                "region_id": len(detections) + 1,
                "x": int(x), "y": int(y), "width": int(w), "height": int(h),
                "area_px": round(float(area), 2),
                "aspect_ratio": round(metrics["aspect_ratio"], 2),
                "perimeter_px": round(metrics["perimeter_px"], 2),
            })

            cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(
                annotated, f"Candidate {len(detections)}",
                (x, max(20, y - 7)), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 1, cv2.LINE_AA
            )

        return annotated, detections
