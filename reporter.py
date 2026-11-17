import csv
import json
from datetime import datetime, timezone
from pathlib import Path

def save_report(image_path, detections, output_dir):
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    payload = {
        "source_image": str(image_path),
        "generated_utc": timestamp,
        "candidate_region_count": len(detections),
        "detections": detections,
        "limitations": (
            "Automated visual screening only. Candidate regions require "
            "review by a qualified inspector or engineer."
        )
    }

    json_path = Path(output_dir) / "crack_inspection_report.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    csv_path = Path(output_dir) / "crack_candidates.csv"
    fields = [
        "region_id", "x", "y", "width", "height",
        "area_px", "aspect_ratio", "perimeter_px"
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(detections)

    return json_path
