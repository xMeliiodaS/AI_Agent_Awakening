import pyautogui
from commands.base_command import BaseCommand


class WindowCommand(BaseCommand):
    def __init__(self, action: str):
        """
        Handles window operations like minimize, maximize, close, or switch.

        :param action: The window action to perform ("minimize", "maximize", "close", "switch").
        """
        super().__init__()
        self.set_params(action=action.lower())
        self.required_params = ["action"]

    def execute_command(self):
        """Executes the specified window action."""
        action = self.params["action"]

        if action == "minimize":
            pyautogui.hotkey("win", "down")  # Minimizes the active window
        elif action == "maximize":
            pyautogui.hotkey("win", "up")  # Maximizes the active window
        elif action == "close":
            pyautogui.hotkey("alt", "f4")  # Closes the active window
        elif action == "switch":
            pyautogui.hotkey("alt", "tab")  # Switches to the next window
        else:
            print(f"Invalid window action: {action}")

        print(f"Executed window action: {action}")

    def undo_command(self):
        """Attempts to reverse the last action where possible."""
        action = self.params["action"]

        if action == "minimize":
            pyautogui.hotkey("alt", "tab")  # Bring back minimized window
        elif action == "maximize":
            pyautogui.hotkey("win", "down")  # Restore window size
        elif action == "close":
            print("Undo not possible for closing a window.")
        elif action == "switch":
            pyautogui.hotkey("shift", "alt", "tab")  # Switch back to the previous window
        else:
            print(f"Undo not available for action: {action}")

# queue.add_command(WindowCommand("minimize"))  # Minimize current window
