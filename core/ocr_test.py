from paddleocr import PaddleOCR
import cv2

# Initialize OCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Path to the captured screenshot
img_path = "../images/screenshot.png"

# Run OCR on the image
result = ocr.ocr(img_path, cls=True)

# Process the result to extract bounding boxes and text
print(result)
for line in result[0]:
    text = line[1]
    bbox = line[0]  # Bounding box coordinates
    print(f"Detected Text: {text}")
    print(f"Bounding Box: {bbox}")
