# define a function
import turtle

def house():
    turtle.begin_fill()
    turtle.forward(141)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()

turtle.width(4)
house()
turtle.goto(-100, -20)
turtle.fillcolor('yellow')
house()

turtle.done()