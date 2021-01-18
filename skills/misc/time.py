import datetime
import random


def time():
    time = datetime.datetime.now().strftime("%H:%M")
    responses = [f"The time is {time}, sir", f"The time is {time}", f"It is {time}, sir", time]
    print(random.choice(responses))
