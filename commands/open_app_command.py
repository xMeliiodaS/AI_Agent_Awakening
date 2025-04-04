import pyautogui
import subprocess
from time import sleep
from commands.base_command import BaseCommand


class OpenAppCommand(BaseCommand):
    def __init__(self, app_name):
        super().__init__()  # Initialize BaseCommand
        self.set_params(app_name=app_name)  # Use the setter to assign parameters
        self.required_params = ["app_name"]  # Ensure app_name is provided

    def execute_command(self):
        app_name = self.params["app_name"]

        pyautogui.press('win')
        sleep(1)
        pyautogui.write(app_name)
        sleep(0.5)
        pyautogui.press('enter')
        print(f"Opening app: {app_name}")

    def undo_command(self):
        # You can use taskkill to close the app (if it's running on Windows).
        app_name = self.params["app_name"]
        subprocess.run(f"taskkill /f /im {app_name}.exe", shell=True)
        print(f"Closing app: {app_name}")
