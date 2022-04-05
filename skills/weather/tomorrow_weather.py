import requests
import random

url = "https://api.openweathermap.org/data/2.5/onecall?lat=51.607999153619204&lon=-0.4052549171747347&appid=24e4c072bb37a84df61ecc02544cdd99"
json_data = requests.get(url).json()


def tomorrow_weather():
    try:
        max_temp = json_data["daily"][1]["temp"]["max"]
        min_temp = json_data["daily"][1]["temp"]["min"]

        max_temp = str(round(max_temp - 273))
        min_temp=str(round(min_temp - 273))

        description=json_data["daily"][1]["weather"][0]["description"]
        if description == "clear":
            description="sunny weather"

        if description == "scattered clouds":
            description="partly sunny weather"

        responses=[
            f"tomorrow in Northwood you can expect {description} with a high of {max_temp} degrees celsius and a low of {min_temp} degrees", f"Tomorrow in Northwood you can expect a high of {max_temp} and a low of {min_temp} degrees with {description}", f"In Northwood tomorrow you can expect {description} with a high of {max_temp} degrees celsius and a low of {min_temp} degrees", f"In Northwood tomorrow you can expect a high of {max_temp} and a low of {min_temp} degrees with {description}"]
        print(random.choice(responses))
    except:
        print("sorry sir, i was unable to get the weather forecast for tomorrow. please check your internet connection and try again")
