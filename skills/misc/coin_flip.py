import random
from output import output

def coin_flip():
    flip_side = random.randint(0, 2)
    if flip_side == 1:
        output("heads")
    else:
        output("tails")
