import requests
import random
import datetime



def current_weather():

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=51.607999153619204&lon=-0.4052549171747347&appid=24e4c072bb37a84df61ecc02544cdd99"
    json_data = requests.get(url).json()

    time = datetime.datetime.now()
    hour = time.strftime("%H")

    hour = int(hour)

    if hour > 15:
        afternoon = True
        num = 24 - hour + 3
        hourly = json_data["hourly"]
        hour_temps = []
        for x in hourly[:num]:
            temp = x["temp"]
            hour_temps.append(temp)
        sum = 0
        for number in hour_temps:
            sum += number
        avg = sum / len(hour_temps)
        night_temp = str(round(avg - 273))
        descriptions = []
        for i in hourly[:num]:
            description = i['weather'][0]["main"]
            descriptions.append(description)
        des_counter = {}
        for word in descriptions:
            if word in des_counter:
                des_counter[word] += 1
            else:
                des_counter[word] = 1
        popular_words = sorted(des_counter, key = des_counter.get, reverse=True)
        night_description = popular_words[:1]
        night_description = night_description[0]
    else:
        afternoon = False


    try:
        temp = json_data["current"]["temp"]

        temp = str(round(temp - 273))

        current_description = json_data["current"]["weather"][0]["main"]

        if current_description == "Clouds":
            curent_description = "cloudy skies"
        if current_description == "Clear":
            current_description = "clear skies"

        min_temp = json_data["daily"][0]["temp"]["min"]
        max_temp = json_data["daily"][0]["temp"]["max"]

        min_temp = str(round(min_temp - 273))
        max_temp = str(round(max_temp - 273))

        description = json_data["daily"][0]["weather"][0]["description"]

        if description == "clear":
            description = "sunny weather"

        if description == "scattered clouds":
            description = "partly sunny weather"

        responses = [f"Currently in Northwood it is {temp} degrees celsius with {current_description}", f"Right now in northwood it is {temp} degrees with {current_description}", f"In Northwood right now it is {temp} degrees with {current_description}", f"Currently in Northwood it is {temp} with {current_description}. Today's forecast you can expect a high of {max_temp} and a low of {min_temp} degrees celsius with {description}"]

        if afternoon:
            responses.pop(3)
            response = f"Currently in Northwood it is {temp} with {current_description}. Tonight you can expect about {night_temp} degrees celsius with {night_description}"
            responses.append(response)
        else:
            pass

        print(random.choice(responses))
    except Exception as e:
        print("sorry sir, i was unable to get the current weather. please check your internet connection and try again")
        print(e)
