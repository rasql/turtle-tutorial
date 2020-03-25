# multiple nested polygons
import turtle

for n in range(3, 7):
    for i in range(n):
        turtle.forward(100)
        turtle.dot()
        turtle.left(360/n)

turtle.done()