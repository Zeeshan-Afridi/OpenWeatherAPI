import requests
import json

API_key = "2a8f13773d1ec72d8c99d504f073861d"
city_name = "Peshawar"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

# url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_key}"


respone = requests.get(url)

data = respone.json()


description = data['weather'][0]["description"]
humidity = data["main"]["humidity"]
temp_min = data['main']['temp_min']
temp_max = data['main']["temp_max"]
temp = data['main']["temp"]

print(f"Maximum Temperature is: {temp_max} \nMinimum Temperature is: {temp_min} \nCurrent Temperature is: {temp}" +
      f"\nCurrent Temperature Description is: {description} \nCurrent Temperature Humidity is: {humidity}")

#Prettify the JSON data by specifying indent level
# formatted_data = json.dumps(data, indent=4)

# print(formatted_data)

