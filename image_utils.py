from pathlib import Path
import cv2

def load_image(path):
    image = cv2.imread(str(path))
    if image is None:
        raise FileNotFoundError(
            f"Could not read image: {path}. Check the path and image format."
        )
    return image

def make_output_dir(path):
    output = Path(path)
    output.mkdir(parents=True, exist_ok=True)
    return output
