# using the ASWD keys to move the turtle
from turtle import *

def move_forward():
    forward(30)

def move_backward():
    backward(30)

def turn_left():
    left(30)

def turn_right():
    right(30)

onkey(move_forward, 'w')
onkey(move_backward, 's')
onkey(turn_left, 'a')
onkey(turn_right, 'd')
listen()

forward(0)
done()
