# using the ASWD keys to move the turtle
import turtle

def forward():
    turtle.forward(30)

def backward():
    turtle.backward(30)

def left():
    turtle.left(30)

def right():
    turtle.right(30)

turtle.onkey(forward, 'w')
turtle.onkey(backward, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.listen()

turtle.forward(0)
turtle.done()
