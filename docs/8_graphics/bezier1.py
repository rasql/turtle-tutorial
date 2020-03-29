# bezier
from turtle import *


for x in range(0, 300, 20):
    y = (300-x)
    goto(x, 0)
    goto(0, y-20)

done()


