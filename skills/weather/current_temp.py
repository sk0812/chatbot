import requests
import random
import datetime

from output import output




def current_temp():

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=51.607999153619204&lon=-0.4052549171747347&appid=24e4c072bb37a84df61ecc02544cdd99"
    json_data = requests.get(url).json()

    try:
        temp = json_data["current"]["temp"]
        temp = str(round(temp - 273))

        responses = [f"Currently in Northwood it is {temp} degrees celsius, sir", f"At the moment it is {temp} degrees, sir", f"Sir, right now it is {temp} degrees", f"it is temp {temp} degrees at the moment, sir"]
        response = random.choice(responses)
        output(response)
    except:
        output("Sorry sir, I was unable to get the current temperature. Please try again later")
