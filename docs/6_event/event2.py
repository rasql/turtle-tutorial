# using the arrow key to move the turtle
import turtle

def forward():
    turtle.forward(30)

def backward():
    turtle.backward(30)

def left():
    turtle.left(30)

def right():
    turtle.right(30)

turtle.onkey(forward, 'Up')
turtle.onkey(backward, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.listen()

turtle.forward(0)
turtle.done()
