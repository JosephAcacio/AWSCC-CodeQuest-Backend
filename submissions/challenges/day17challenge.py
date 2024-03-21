import requests

endpoint = requests.get("https://jsonplaceholder.typicode.com/");

if endpoint.status_code == 200:
    print("Request Successful")
else:
    print("Request Failed")



