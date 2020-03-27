# controlling two turtles
from turtle import *

x = 0
y = 0
d = 20

def up():
    global y
    y = y + d
    setposition(x, y)

def down():
    global y
    y = y - d
    setposition(x, y)

def left():
    global x
    x = x - d
    setposition(x, y)

def right():
    global x
    x = x + d
    setposition(x, y)

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

listen()
forward(0)
done()
