import requests
import json

# add your openweahter api key here
API_key = API
city_name = "Peshawar"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

#access the url
respone = requests.get(url)

# get the data from the respose in json formate
data = respone.json()

# access targeted attributes and store it in variables
description = data['weather'][0]["description"]
humidity = data["main"]["humidity"]
temp_min = data['main']['temp_min']
temp_max = data['main']["temp_max"]
temp = data['main']["temp"]

# print the attributes
print(f"Maximum Temperature is: {temp_max} \nMinimum Temperature is: {temp_min} \nCurrent Temperature is: {temp}" +
      f"\nCurrent Temperature Description is: {description} \nCurrent Temperature Humidity is: {humidity}")
