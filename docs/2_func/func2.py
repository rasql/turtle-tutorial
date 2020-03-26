# define a function
import turtle

def side():
    turtle.forward(100)
    turtle.left(90)

def square():
    side()
    side()
    side()
    side()
    turtle.forward(100)

square()
square()
square()

turtle.done()