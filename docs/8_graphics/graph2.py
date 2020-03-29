# triangle
from turtle import *

color('red')

def triangle(x):
    if x < 20:
        begin_fill()
        for i in range(3):
            forward(x)
            left(360/3)
        end_fill()
    else:
        for i in range(3):
            triangle(x/2)
            forward(x)
            left(360/3)

speed(10)
hideturtle()

triangle(200)
done()