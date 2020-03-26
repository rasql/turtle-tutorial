# variable used inside a function
import turtle

def triangle():
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)

a = 50
triangle()
a = 100
triangle()
a = 150
triangle()

turtle.done()