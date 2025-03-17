# import requests
#
# url = "http://127.0.0.1:1234/v1/chat/completions"
# headers = {"Content-Type": "application/json"}
# data = {
#     "model": "deepseek-r1-distill-qwen-7b",
#     "messages": [{"role": "user", "content": "What name I mentioned in the last message?"}]
# }
#
# response = requests.post(url, headers=headers, json=data)
#
# json_response = response.json()
# clean_response = json_response['choices'][0]['message']['content']
# print(clean_response)

import requests
import base64

# API Endpoint (Check if the port is correct)
url = "http://127.0.0.1:1234/v1/chat/completions"

# Headers for JSON data
headers = {"Content-Type": "application/json"}

# Define the image path
image_path = "../images/screenshot.png"

# Read and encode the image in Base64
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Construct the request payload
data = {
    "model": "llava-1.6-7b",
    "messages": [
        {
            "role": "user",
            "content": (
                "Analyze the given image and determine if the application is currently loading. "
                "A system is loading if essential UI elements (e.g., text, buttons, lists) are missing, "
                "if there are placeholders, progress bars, or 'Loading...' messages. "
                "Ignore minor animations like activity indicators (e.g., Discord’s spinning wheel). "
                "Provide a clear answer: 'Yes (Loading)' or 'No (Not Loading)', with a brief explanation."
            ),
            "image": {"type": "base64", "data": base64_image}  # Attach base64 image
        }
    ],
}

# Send the request
response = requests.post(url, headers=headers, json=data)

# Print the full response to debug
json_response = response.json()

# Check for the 'choices' key in the response and handle accordingly
if 'choices' in json_response:
    clean_response = json_response['choices'][0]['message']['content']
    print(clean_response)
else:
    print("Response does not contain 'choices' key. Full response:", json_response)
