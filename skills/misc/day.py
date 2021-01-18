import datetime
import random

def day():
    current = datetime.datetime.now()
    day = current.strftime("%A")
    responses = [f"Today is {day}, sir", f"It is {day} today", f"Sir, today is {day}", f"It is {day}, sir"]
    print(random.choice(responses))
