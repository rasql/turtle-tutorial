# using the arrow key to move the turtle
from turtle import *

def move_forward():
    forward(30)

def move_backward():
    backward(30)

def turn_left():
    left(30)

def turn_right():
    right(30)

onkey(move_forward, 'Up')
onkey(move_backward, 'Down')
onkey(turn_left, 'Left')
onkey(turn_right, 'Right')
listen()

forward(0)
done()
