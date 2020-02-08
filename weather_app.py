import json, requests

key = "Enter Yuor API Key"

base_URL = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "Enter the City name: "

#complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

final_url = base_URL +  "&q=" + {city name},{country code} + "&appid=" + "key"

res = requests.get(complete_url)

x = response.json()

if x["cod"] ! = "200":
     y = x["main"]
     current_temperature = y["temp"]
      z = x["weather"]
       weather_description = z[0]["description"]
       print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n description = " +
                    str(weather_description))

       else:
           print ("City not found")
           
