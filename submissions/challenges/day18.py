import requests

api_url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "User-Agent": "MyApp/1.0"
}

response = requests.get(api_url, headers=headers)

print(f"Status code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Content: {response.json()}")

data = {
    "title": "hirap naman nito",
    "body": "masculine"
}

post_response = requests.post(api_url, json=data, headers=headers)
print(f"Status Code: {post_response.status_code}")
print(f"Response Content: {post_response.json()}")
