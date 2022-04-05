import random

def what_can_you_do():
    print("A few things you can ask me are: ")
    responses = ["How is the weather tomorrow", "Open youtube", "what is the time", "what day is it", "heads or tails", "roll a dice", "how is the current weather", "how is the weather today", "search youtube for cricket highlights", "search amazon for light bulbs", "search ebay for used tennis racquet", "search google for how to solve the rubiks cube", "pick a random number between 1 and 10", "ooen microsoft word"]
    choices = random.sample(responses, 3)
    for choice in choices:
        print(choice)
