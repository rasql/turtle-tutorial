# controlling two turtles
from turtle import *

def move(x, y):
    setposition(x, y)

onscreenclick(move)
listen()

forward(0)
done()
