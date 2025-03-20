import pyautogui
from commands.base_command import BaseCommand


class ScrollCommand(BaseCommand):
    def __init__(self, direction: str, amount: int = 1):
        """
        Scrolls the screen in the specified direction.

        :param direction: "up" or "down".
        :param amount: Number of scroll steps.
        """
        super().__init__()
        self.set_params(direction=direction.lower(), amount=amount)
        self.required_params = ["direction", "amount"]  # Ensure required params are set

    def execute_command(self):
        """Executes the scroll action."""
        direction = self.params["direction"]
        amount = self.params["amount"]

        scroll_value = amount if direction == "up" else -amount
        pyautogui.scroll(scroll_value)
        print(f"Scrolling {direction} by {amount} steps.")

    def undo_command(self):
        """Reverses the last scroll action."""
        direction = "down" if self.params["direction"] == "up" else "up"
        amount = self.params["amount"]

        reverse_scroll_value = amount if direction == "up" else -amount
        pyautogui.scroll(reverse_scroll_value)
        print(f"Undoing scroll: Scrolling {direction} by {amount} steps.")

# queue.add_command(ScrollCommand("down", 5))  # Scrolls down 5 steps
# queue.add_command(ScrollCommand("up", 3))    # Scrolls up 3 steps
