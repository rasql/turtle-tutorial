# https://en.wikipedia.org/wiki/Minkowski_Sausage
from turtle import *

turns = (1, -1, -1, 0, 1, 1, -1, 0)

def curve(x):
    if x < 20:
        forward(x)
    else:
        for t in turns:
            curve(x/4)
            if t == 1:
                left(90)
            elif t== -1:
                right(90)        

speed(10)
hideturtle()

curve(400)
done()