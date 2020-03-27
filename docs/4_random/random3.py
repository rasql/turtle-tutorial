# random dot size
from turtle import *
import random

dot()
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    size = random.randint(10, 50)  
    goto(x, y)
    dot(size)

done()
    