# -------------------------------- API -----------------------------------------
import json

import datetime as dt
import requests
MY_LAT = 13.008886
MY_LONG = 77.540152

'''Requesting coordinates from International space station'''
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("The resource doesn't exist")
# # if response.status_code == 401:
# #     raise Exception("Your are not authorised to access this data")
# response.raise_for_status()
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# coordinates = (latitude,longitude)
# print(coordinates)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")


print(sunrise[0])
print(sunset[0])
now = dt.datetime.now()
print(now.hour)

# print(response.json())
# with open("data.json",mode="w") as data:
#     json.dumps(response.json())

