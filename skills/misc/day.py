import datetime
import random

from output import output

def day():
    current = datetime.datetime.now()
    day = current.strftime("%A")
    responses = [f"Today is {day}, sir", f"It is {day} today", f"Sir, today is {day}", f"It is {day}, sir"]
    response = random.choice(responses)
    output(response)
