# triangle
from turtle import *

def triangle(x):
    for i in range(3):
        if x > 20:
            triangle(x/2)
        forward(x)
        left(360/3)

speed(10)
hideturtle()

triangle(200)
done()