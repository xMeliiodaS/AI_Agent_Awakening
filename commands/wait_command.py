import time
import pyautogui
from PIL import ImageChops
from commands.base_command import BaseCommand


class WaitCommand(BaseCommand):
    def __init__(self, timeout=30, check_interval=1, use_ai=False):
        super().__init__()
        self.set_params(timeout=timeout, check_interval=check_interval, use_ai=use_ai)
        self.required_params = ["timeout", "check_interval", "use_ai"]

    def execute_command(self):
        timeout = self.params["timeout"]
        check_interval = self.params["check_interval"]
        use_ai = self.params["use_ai"]

        if use_ai:
            print("Waiting using AI detection (to be integrated).")
            self.wait_using_ai(timeout)
        else:
            print("Waiting using basic screen comparison.")
            self.wait_using_screen_comparison(timeout, check_interval)

    @staticmethod
    def wait_using_screen_comparison(timeout, check_interval):
        # Step 1: Capture initial screen
        initial_screen = pyautogui.screenshot()
        start_time = time.time()

        # Step 2: Wait and continuously check for changes in the screen
        while time.time() - start_time < timeout:
            current_screen = pyautogui.screenshot()

            # Compare the initial and current screenshots
            diff = ImageChops.difference(initial_screen, current_screen)

            if diff.getbbox():  # If there's a difference in images (non-empty bounding box)
                print("Change detected! Loading complete.")
                return  # Exit the wait command if change detected

            time.sleep(check_interval)  # Wait before checking again

        print(f"Timeout reached: {timeout} seconds. No change detected.")

    @staticmethod
    def wait_using_ai(timeout):
        # Placeholder function for AI-based detection.
        # Once AI is integrated, this function will use the AI to detect loading states.
        print("This is where AI will handle the waiting logic.")
        print(f"Waiting for AI to detect loading status for up to {timeout} seconds...")

        # For now, we simulate a wait period
        time.sleep(timeout)
        print("AI detected loading completion.")
