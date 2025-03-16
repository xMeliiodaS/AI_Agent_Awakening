import time
from core.coordinate_finder import OCRProcessor
from commands.click_command import ClickCommand
from commands.open_app_command import OpenAppCommand


def run_main_flow(param_image_path, param_search_word, param_template_path, app_name):
    ocr_processor = OCRProcessor(lang='en')

    # Get coordinates from OCR
    coordinates = ocr_processor.get_coordinates_from_ocr(param_image_path, param_search_word)
    if coordinates:  # Check if coordinates are found
        x, y, _ = coordinates[0]  # Take the first found coordinate
        test_click_command(x, y)
    else:
        print(f"Text '{param_search_word}' not found in the image.")
    # test_open_app_command(app_name)


def test_click_command(x, y):
    click_cmd = ClickCommand(x, y)
    click_cmd.execute_command()  # Execute click command at the coordinates
    time.sleep(0.2)
    click_cmd.execute_command()  # Execute click command at the coordinates

def test_open_app_command(app_name):
    open_app_cmd = OpenAppCommand(app_name)
    open_app_cmd.execute_command()


def main():
    image_path = "images/screenshot.png"
    template_path = "button_template.png"  # Only if you're using template matching for graphics
    search_word = "Edge"  # The word we want to search for and click
    app_name = "chrome"

    # Running the flow with both OCR and image recognition
    run_main_flow(image_path, search_word, template_path, app_name)


if __name__ == "__main__":
    main()

