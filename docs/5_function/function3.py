# star function with 4 arguments
import turtle

def star(n, m, a, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(a)
        turtle.dot()
        turtle.left(360/n*m)
    turtle.end_fill()

turtle.back(200)
star(5, 2, 100, 'red')

turtle.forward(150)
star(7, 3, 120, 'blue')

turtle.forward(160)
star(11, 6, 120, 'yellow')

turtle.done()