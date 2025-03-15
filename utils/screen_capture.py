import mss
import cv2
import numpy as np

# Initialize screen capture
with mss.mss() as sct:
    # Capture screen
    screenshot = sct.shot(output="screenshot.png")


# import mss
# import cv2
# import numpy as np
#
# # Initialize screen capture
# with mss.mss() as sct:
#     # Define the monitor or area of the screen to capture (full screen or custom region)
#     monitor = sct.monitors[1]  # or you can use a specific monitor number for multi-monitor setup
#     screenshot = sct.grab(monitor)
#
#     # Convert to an image using numpy array
#     img = np.array(screenshot)
#
#     # Resize the image to a higher resolution (e.g., double the size)
#     new_dim = (img.shape[1] * 2, img.shape[0] * 2)  # Increase size by 2x
#     resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_CUBIC)
#
#     # Save the resized screenshot to a file
#     cv2.imwrite("high_res_screenshot.png", resized_img)
#
# # Now you can pass this high-res image to PaddleOCR for better accuracy
