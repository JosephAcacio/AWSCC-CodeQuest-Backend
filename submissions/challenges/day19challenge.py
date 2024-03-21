import requests

api_endpoint = "https://api.spacexdata.com/v5/launches/latest"

response =  requests.get(api_endpoint)



if response.status_code == 200:
    print(f"Status code: {response.status_code}")
    data =  response.json()

    flight_number = data['flight_number']
    mission_name = data["name"]
    launch_details = data['success']

    print(f"Flight number: {flight_number}")
    print(f"Mission name: {mission_name}")
    print(f"Launch details: {launch_details}")
else:
    print(f"Status Code Error: {response.status_code}")