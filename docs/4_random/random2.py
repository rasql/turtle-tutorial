# random direction
from turtle import *
import random

dot()
for i in range(100):
    angle = random.randint(-90, 90)
    forward(20)
    left(angle)
    dot()

done()