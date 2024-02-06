import requests
import json
import os
city = input("Enter the City Name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r = requests.get(url)
w_dic = json.loads(r.text)
print("Temperature is : ",w_dic["current"]["temp_c"])
temp = w_dic["current"]["temp_c"]
os.system(f"say 'The Temperature of {city} is: {temp} degrees Celsius'")
