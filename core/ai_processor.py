import requests

url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [{"role": "user", "content": "What name I mentioned in the last message?"}]
}

response = requests.post(url, headers=headers, json=data)

json_response = response.json()
clean_response = json_response['choices'][0]['message']['content']
print(clean_response)
