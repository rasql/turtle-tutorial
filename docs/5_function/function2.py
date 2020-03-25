# polygon function with arguments
import turtle

def polygon(n, a):
    for i in range(n):
        turtle.forward(a)
        turtle.dot()
        turtle.left(360/n)

turtle.back(200)
polygon(3, 80)

turtle.forward(150)
polygon(5, 80)

turtle.forward(200)
polygon(9, 40)

turtle.done()