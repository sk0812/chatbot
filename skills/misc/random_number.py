import random
import re

def random_number(text):
    text = [int(s) for s in text.split() if s.isdigit()]
    text = sorted(text)
    num_1 = text[0]
    num_2 = text[1]
    print(random.randint(num_1, num_2))
