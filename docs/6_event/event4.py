# using key events with a lambda function
from turtle import *

onkey(lambda: forward(30), 'Up')
onkey(lambda: backward(30), 'Down')
onkey(lambda: left(30), 'Left')
onkey(lambda: right(30), 'Right')
listen()

forward(0)
done()
