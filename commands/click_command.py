import pyautogui
from time import sleep
from commands.base_command import BaseCommand


class ClickCommand(BaseCommand):
    def __init__(self, x, y, smooth=False, duration=0.5):
        super().__init__(x=x, y=y, smooth=smooth, duration=duration)
        self.required_params = ["x", "y"]  # Ensure x and y are provided

    def execute_command(self):
        x, y = self.params["x"], self.params["y"]
        smooth = self.params.get("smooth", False)
        duration = self.params.get("duration", 0.5)

        if smooth:
            pyautogui.moveTo(x, y, duration=duration)  # Smooth movement
        pyautogui.click(x, y)

        print(f"Clicking at ({x}, {y}) with{' smooth' if smooth else 'out'} movement.")

    def undo_command(self):
        print("Undoing click...")  # You can implement an undo for click if needed
