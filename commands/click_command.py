import pyautogui
from time import sleep
from commands.base_command import BaseCommand


class ClickCommand(BaseCommand):
    def __init__(self, x, y):
        super().__init__(x=x, y=y)
        self.required_params = ["x", "y"]  # Ensure x and y are provided

    def execute(self):
        x, y = self.params["x"], self.params["y"]
        pyautogui.click(x, y)
        print(f"Clicking at ({x}, {y})")

    def undo(self):
        print("Undoing click...")  # You can implement an undo for click if needed
