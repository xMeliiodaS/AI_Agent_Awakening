import pyautogui
from commands.base_command import BaseCommand


class HotkeyCommand(BaseCommand):
    def __init__(self, *keys):
        """
        Executes a keyboard hotkey (e.g., Ctrl+C, Alt+Tab).

        :param keys: A sequence of keys to press simultaneously.
        """
        super().__init__()
        self.set_params(keys=list(keys))  # Store keys as a list
        self.required_params = ["keys"]  # Ensure keys are provided

    def execute_command(self):
        """Executes the hotkey combination."""
        keys = self.params["keys"]
        pyautogui.hotkey(*keys)
        print(f"Executed hotkey: {' + '.join(keys)}")

    def undo_command(self):
        pass
