# controlling two turtles
import turtle

def move(x, y):
    turtle.setposition(x, y)

turtle.onscreenclick(move)
turtle.listen()

turtle.forward(0)
turtle.done()
