import requests
import random
import datetime

from output import output



def tonight_weather():

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=51.607999153619204&lon=-0.4052549171747347&appid=24e4c072bb37a84df61ecc02544cdd99"
    json_data = requests.get(url).json()

    time = datetime.datetime.now()
    hour = time.strftime("%H")
    hour = int(hour)
    hourly = json_data['hourly']
    hour_temp = []
    descriptions = []
    if hour < 20:
        night = False
        hour_count = 20 - hour
        for x in hourly[hour_count:hour_count+7]:
            temp = x['temp']
            hour_temp.append(temp)
    else:
        night = True
        hour_count = 24 - hour + 3
        for x in hourly[hour:hour_count + hour]:
            temp = x['temp']
            hour_temp.append(temp)
    sum = 0
    for num in hour_temp:
        sum += num
    avg = sum / len(hour_temp)
    temp = str(round(avg - 273))

    if night:
        for i in hourly[hour:hour_count + hour]:
            description = i['weather'][0]["main"]
            descriptions.append(description)
    else:
        for i in hourly[hour_count:hour_count+7]:
            description = i['weather'][0]["main"]
            descriptions.append(description)
    des_counter = {}
    for word in descriptions:
        if word in des_counter:
            des_counter[word] += 1
        else:
            des_counter[word] = 1
    popular_words = sorted(des_counter, key = des_counter.get, reverse=True)
    description = popular_words[:1]
    description = description[0].lower()

    if description == "rain":
        d2 = "rainy"
    elif description == "clouds":
        d2 = "cloudy"

    responses = [f"Tonight it is {temp} degrees with {description}, sir", f"Sir, tonight it is {temp} degrees with {description}", f"Sir, tonight you can expect {d2} weather with temperatures of {temp} degrees celsius", f"Tonight's forecast it is {temp} degrees with {d2} weather, sir", f"The forescast for tonight is {temp} degrees with {description}"]
    response = random.choice(responses)
    output(response)
