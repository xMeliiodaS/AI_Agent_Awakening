import cv2
import pyautogui
import numpy as np

# Load the template image (e.g., button icon)
template = cv2.imread('button_template.png', 0)

# Capture the screenshot of the screen (you can use the same screen capture from before)
img = cv2.imread("../images/high_res_screenshot.png", 0)

# Perform template matching
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# Get the location of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Coordinates of the top-left corner of the matching region
top_left = max_loc
print(f"Best match found at: {top_left}")

# Draw a rectangle around the matched area (for visualization)
h, w = template.shape
cv2.rectangle(img, top_left, (top_left[0] + w, top_left[1] + h), 255, 2)

# Save the result for visual check (optional)
cv2.imwrite('match_result.png', img)

# Calculate the center of the matched area (for clicking)
center_x = top_left[0] + w // 2
center_y = top_left[1] + h // 2

# Move the mouse to the button location using pyautogui
pyautogui.moveTo(center_x, center_y, duration=1)  # Move to the position over 1 second
pyautogui.click()  # Click the position
