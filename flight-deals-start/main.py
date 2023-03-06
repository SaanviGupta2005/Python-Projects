from pprint import pprint
import requests

sheet_endpoint ="https://api.sheety.co/f11200b3262cc36f60f567b0b5a40e28/flightDeals/prices"

sheet_response = requests.get(sheet_endpoint)
data = sheet_response.json()

sheet_data = data["prices"]
print(sheet_data)



