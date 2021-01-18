import requests
import random

url = "https://api.openweathermap.org/data/2.5/onecall?lat=51.607999153619204&lon=-0.4052549171747347&appid=24e4c072bb37a84df61ecc02544cdd99"
json_data = requests.get(url).json()

def today_weather():
    try:
        min_temp = json_data["daily"][0]["temp"]["min"]
        max_temp = json_data["daily"][0]["temp"]["max"]

        min_temp = str(round(min_temp - 273))
        max_temp = str(round(max_temp - 273))

        description = json_data["daily"][0]["weather"][0]["description"]

        if description == "clear":
            description = "sunny weather"

        if description == "scattered clouds":
            description = "partly sunny weather"
        responses = [f"today's forecast you can expect {description} with a high of {max_temp} degrees and a low of {min_temp}", f"Today in Northwood you can experience {description} with a high of {max_temp} and a low of {min_temp} degrees celsius", f"Today's forecast in Northwood you can expect {description} with a high of {max_temp} degrees and a low of {min_temp}"]
        print(random.choice(responses))
    except:
        print("sorry sir, i was unable to get today's weather forecast. please check your internet connection and try again")
