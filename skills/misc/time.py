import datetime
import random

from output import output

def time():
    time = datetime.datetime.now().strftime("%H:%M")
    responses = [f"The time is {time}, sir", f"The time is {time}", f"It is {time}, sir", time]
    response = random.choice(responses)
    output(response)
