import pyautogui
from commands.base_command import BaseCommand

class TypeTextCommand(BaseCommand):
    def __init__(self, text):
        super().__init__(text=text)
        self.required_params = ["text"]  # Ensure text is provided

    def execute(self):
        text = self.params["text"]
        pyautogui.write(text)  # Types the text at the currently focused field
        print(f"Typing text: '{text}'")

    def undo(self):
        print("Undoing text input...")  # Optionally implement undo logic