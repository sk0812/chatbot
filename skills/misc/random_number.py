import random

from output import output

def random_number(text):
    text = [int(s) for s in text.split() if s.isdigit()]
    text = sorted(text)
    num_1 = text[0]
    num_2 = text[1]
    output(random.randrange(num_1, num_2))
