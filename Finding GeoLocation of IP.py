import json
import requests
#Google What is my ip address and replace 63.70.164.200
response = requests.get("http://extreme-ip-lookup.com/json/63.70.164.200")
print('Response Code: {}' .format(response.status_code))
todos = json.loads(response.text)
print('businessName: {}'.format(response.json()["businessName"]))
print('businessWebsite: {}'.format(response.json()["businessWebsite"]))
print('city: {}'.format(response.json()["city"]))
print('continent: {}'.format(response.json()["continent"]))
print('countryCode: {}'.format(response.json()["countryCode"]))
print('ipName: {}'.format(response.json()["ipName"]))
print('ipType: {}'.format(response.json()["ipType"]))
print('lat: {}'.format(response.json()["lat"]))
print('lon: {}'.format(response.json()["lon"]))
print('query: {}'.format(response.json()["query"]))
print('region: {}'.format(response.json()["region"]))
