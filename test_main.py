import time
from core.coordinate_finder import OCRProcessor
from commands.click_command import ClickCommand


def run_main_flow(param_image_path, param_search_word, param_template_path):
    ocr_processor = OCRProcessor(lang='en')

    # Get coordinates from OCR
    coordinates = ocr_processor.get_coordinates_from_ocr(param_image_path, param_search_word)
    if coordinates:  # Check if coordinates are found
        x, y, _ = coordinates[0]  # Take the first found coordinate
        test_click_command(x, y)
    else:
        print(f"Text '{param_search_word}' not found in the image.")


def test_click_command(x, y):
    click_cmd = ClickCommand(x, y)
    click_cmd.execute_command()  # Execute click command at the coordinates
    time.sleep(0.2)
    click_cmd.execute_command()  # Execute click command at the coordinates


def main():
    image_path = "images/screenshot.png"
    template_path = "button_template.png"  # Only if you're using template matching for graphics
    search_word = "Edge"  # The word we want to search for and click

    # Running the flow with both OCR and image recognition
    run_main_flow(image_path, search_word, template_path)


if __name__ == "__main__":
    main()

