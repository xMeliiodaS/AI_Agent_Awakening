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
# data = {
#     "model": "llava-1.6-7b",
#     "messages": [
#         {
#             "role": "user",
#             "content": (
#                 "Analyze the provided image carefully and determine if the application is currently in a loading state. "
#                 "The application is considered 'loading' ONLY if the image displays clear, definitive loading indicators, "
#                 "such as a percentage (e.g., '50%'), a progress bar, or explicit 'Please Wait' or 'loading' messages or similar texts. "
#                 "Other indicators, such as a spinning wheel or minor animations, should NOT be considered as signs of loading. "
#                 "The absence of UI elements or a blank screen does NOT automatically indicate loading. "
#                 "The screen must explicitly show content indicating the application is processing, retrieving, or waiting for something. "
#                 "Only if these types of loading indicators are clearly visible, respond with 'Yes (Loading)'. If no such indicators are visible, respond with 'No (Not Loading)'. "
#                 "Please make sure that the response is clear and not based on assumptions about the application being idle or lacking UI elements. "
#                 "Provide the response followed by a brief explanation that justifies your answer based on visible loading indicators or the lack thereof. "
#                 "If the screen is currently on the Desktop, then it's probably not loading. "
#                 "Ignore any progress bar at the bottom of the screen."
#             ),
#             "image": {"type": "base64", "data": base64_image}  # Attach base64 image
#         }
#     ],
# }

data = {
    "model": "llava-1.6-7b",
    "messages": [
        {
            "role": "user",
            "content": (
                "Hey, My name is Bahaa"
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
