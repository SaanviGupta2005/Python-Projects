import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "saanvi"
TOKEN = "hjkfj354jnf952g8kfk20fj"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")

post_pixel_data = {
    "date": DATE,
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
print(response.text)

# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
#
# update_pixel_data = {
#     "quantity": "18"
# }
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
