# polygon function without arguments
from turtle import *
import random

def hexagon():
    for i in range(6):
        forward(30)
        left(60)

for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    goto(x, y)
    hexagon()

done()