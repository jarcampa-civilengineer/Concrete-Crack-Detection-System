import argparse
from pathlib import Path
import cv2
from detector import CrackDetector
from reporter import save_report
from image_utils import load_image, make_output_dir

def main():
    parser = argparse.ArgumentParser(description="Concrete crack visual screening tool")
    parser.add_argument("--image", required=True, help="Path to an inspection image")
    parser.add_argument("--output", default="outputs", help="Output folder")
    parser.add_argument("--min-area", type=int, default=30, help="Minimum contour area in pixels")
    args = parser.parse_args()

    image_path = Path(args.image)
    image = load_image(image_path)
    detector = CrackDetector(min_area=args.min_area)
    annotated, detections = detector.detect(image)

    output_dir = make_output_dir(args.output)
    annotated_path = output_dir / f"{image_path.stem}_crack_detection.jpg"
    cv2.imwrite(str(annotated_path), annotated)
    report_path = save_report(image_path, detections, output_dir)

    print(f"Image processed: {image_path}")
    print(f"Candidate regions: {len(detections)}")
    print(f"Annotated image: {annotated_path}")
    print(f"Report: {report_path}")
    print("Reminder: detections are visual candidates, not confirmed structural cracks.")

if __name__ == "__main__":
    main()
