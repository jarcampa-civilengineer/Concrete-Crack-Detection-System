import cv2

def contour_metrics(contour):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    x, y, width, height = cv2.boundingRect(contour)
    short_side = max(1, min(width, height))
    long_side = max(width, height)
    return {
        "area_px": area,
        "perimeter_px": perimeter,
        "aspect_ratio": long_side / short_side,
        "width_px": width,
        "height_px": height,
    }

def pixels_to_mm(pixel_length, pixels_per_mm):
    """Convert pixels to mm only when a valid image scale is known."""
    if pixels_per_mm <= 0:
        raise ValueError("pixels_per_mm must be greater than zero.")
    return pixel_length / pixels_per_mm
