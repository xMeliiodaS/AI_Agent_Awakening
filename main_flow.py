from core.coordinate_finder import get_coordinates_from_ocr, get_coordinates_from_template
from commands.simulate_mouse_click import simulate_move_and_click, simulate_double_click


def run_main_flow(image_path, search_word, template_path=None):
    """
    Runs the main flow to search for the given word (search_word) in the image and click on it.
    If OCR doesn't detect it, template matching is used.

    :param image_path: Path to the image to process.
    :param search_word: The word to search for in the image using OCR.
    :param template_path: (Optional) Path to template image for template matching.
    """


    # First, attempt to use OCR to find text elements
    ocr_coordinates = get_coordinates_from_ocr(image_path, search_word)

    if ocr_coordinates:
        # Use OCR coordinates if text was detected
        for x, y, text in ocr_coordinates:
            print(f"Simulating click at ({x}, {y}) with detected text: {text}")
            # simulate_move_and_click(x, y)
            simulate_double_click(x, y)
    else:
        # If OCR didn't detect text, use image recognition (template matching)
        if template_path:
            image_coordinates = get_coordinates_from_template(image_path, template_path)
            for x, y in image_coordinates:
                print(f"Simulating click at ({x}, {y}) using template recognition.")
                simulate_move_and_click(x, y)


# Example usage:
image_path = "images/screenshot.png"
template_path = "button_template.png"  # Only if you're using template matching for graphics
search_word = "Discord"  # The word we want to search for and click

# Running the flow with both OCR and image recognition
run_main_flow(image_path, search_word, template_path)
