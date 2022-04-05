import random


def coin_flip():
    flip_side = random.randint(0, 2)
    if flip_side == 1:
        print("heads")
    else:
        print("tails")
