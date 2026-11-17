from pathlib import Path

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

def validate_image_path(path):
    image_path = Path(path)
    if not image_path.exists() or not image_path.is_file():
        raise FileNotFoundError(f"Image file does not exist: {image_path}")
    if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported image type: {image_path.suffix}")
    return image_path
