# Concrete Crack Detection System

A small Python image-processing prototype that flags dark, elongated surface
features in concrete photographs for preliminary inspection.

## Features

- Processes an inspection image using OpenCV.
- Enhances local contrast and extracts dark linear candidates.
- Draws bounding boxes around candidate regions.
- Exports a JSON inspection summary and CSV candidate list.
- Reports image-space dimensions and shape metrics in pixels.

## Project structure

- `main.py` — command-line entry point
- `detector.py` — image processing and candidate extraction
- `image_utils.py` — image loading and output folder handling
- `measurements.py` — contour geometry and optional scale conversion
- `reporter.py` — JSON and CSV report generation
- `validators.py` — image path/type validation
- `requirements.txt` — dependencies

## Installation

Python 3.10+ recommended.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\\Scripts\\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install packages:
```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py --image samples/concrete_wall.jpg
```

Choose another output folder:
```bash
python main.py --image samples/concrete_wall.jpg --output inspection_results
```

Adjust minimum contour area:
```bash
python main.py --image samples/concrete_wall.jpg --min-area 50
```

The output folder contains:
- `*_crack_detection.jpg` — annotated image
- `crack_inspection_report.json` — inspection metadata and findings
- `crack_candidates.csv` — candidate region measurements in pixels

## Important engineering limitations

This is a baseline image-processing demonstration, not a validated crack
measurement or structural-condition assessment system. Shadows, formwork
lines, joints, stains, aggregate texture, and surface defects may be flagged;
fine cracks may also be missed. Pixel measurements are not physical crack
widths or lengths unless the image is calibrated using a known scale and
appropriate imaging geometry. For reliable crack classification, train and
validate a segmentation model using representative, expert-labeled concrete
images. Verify findings in the field and follow applicable inspection
standards and engineering judgment. Do not use this prototype alone to
determine structural safety or repair requirements.
