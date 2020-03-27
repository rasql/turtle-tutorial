# controlling two turtles
import turtle

x = 0
y = 0
d = 20

def up():
    global y
    y = y + d
    turtle.setposition(x, y)

def down():
    global y
    y = y - d
    turtle.setposition(x, y)

def left():
    global x
    x = x - d
    turtle.setposition(x, y)

def right():
    global x
    x = x + d
    turtle.setposition(x, y)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.listen()
turtle.forward(0)
turtle.done()
