# draw a parallelogram
import turtle

a = 200
b = 150
angle = 60

turtle.forward(a)
turtle.left(angle)
turtle.forward(b)
turtle.left(180-angle)
turtle.forward(a)
turtle.left(angle)
turtle.forward(b)
turtle.left(180-angle)

turtle.done()
