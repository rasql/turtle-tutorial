# https://en.wikipedia.org/wiki/Minkowski_Sausage
from turtle import *

color('red')

def curve(x):
    if x < 20:
        forward(x)
    else:
        curve(x/3)
        left(90)
        curve(x/3)
        right(90)
        curve(x/3)
        right(90)
        curve(x/3)
        left(90)
        curve(x/3)
        

speed(10)
hideturtle()

curve(200)
done()