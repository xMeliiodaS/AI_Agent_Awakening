import pyautogui
import time


def simulate_move_and_click(x, y):
    # Move the mouse and click
    pyautogui.moveTo(x, y, duration=1)  # Move smoothly to the target position
    time.sleep(0.2)  # Wait for half a second before clicking
    pyautogui.click()  # Simulate the click


def simulate_double_click(x, y):
    # Move the mouse to (x, y) with a smooth transition (duration of 1 second)
    pyautogui.moveTo(x, y, duration=1)

    # Perform the first click
    pyautogui.click()

    # Wait for a short period before the second click (double-click speed)
    time.sleep(0.25)  # You can adjust this delay if needed

    # Perform the second click (double-click)
    pyautogui.click()
