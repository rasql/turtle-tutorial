# using various keys to control the turtle
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

turtle.onkey(turtle.home, 'h')
turtle.onkey(turtle.clear, 'c')
turtle.onkey(turtle.reset, 'r')
turtle.onkey(turtle.bye, 'q')

turtle.onkey(turtle.up, 'u')
turtle.onkey(turtle.down, 'd')

turtle.listen()

turtle.forward(0)
turtle.done()
