import cv2
from paddleocr import PaddleOCR
import numpy as np


class OCRProcessor:
    def __init__(self, lang='en'):
        self.ocr = PaddleOCR(use_angle_cls=True, lang=lang)  # Initialize OCR with language option

    def get_coordinates_from_ocr(self, image_path, search_word):
        """
        Uses OCR to find specific text (search_word) in the image and returns its coordinates.

        :param image_path: Path to the image to process.
        :param search_word: The word to search for in the image using OCR.
        :return: A list of (x, y, text) tuples where text matches the search_word.
        """
        result = self.ocr.ocr(image_path, cls=True)
        coordinates = []

        # Loop through detected text and filter by the search word
        for line in result[0]:
            detected_text = line[1][0]
            if search_word.lower() in detected_text.lower():  # Case insensitive search
                bounding_box = line[0]
                # Calculate the center of the bounding box
                x_center = (bounding_box[0][0] + bounding_box[2][0]) / 2
                y_center = (bounding_box[0][1] + bounding_box[2][1]) / 2
                coordinates.append((x_center, y_center, detected_text))

        print(coordinates)
        return coordinates

    @staticmethod
    def get_coordinates_from_template(image_path, template_path):
        """
        Uses template matching to find coordinates of a template in an image.

        :param image_path: Path to the image to process.
        :param template_path: Path to the template to search for.
        :return: A list of coordinates where the template matches.
        """
        img = cv2.imread(image_path)
        template = cv2.imread(template_path)

        # Match the template with the image
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Coordinates of the top-left corner of the match
        top_left = max_loc
        w, h = template.shape[1], template.shape[0]

        # Calculate the center of the matched region
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2

        return [(center_x, center_y)]  # Return as a list of coordinates
