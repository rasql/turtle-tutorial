# drawing a star
import turtle

a = 200
n = 11
m = 4

turtle.begin_fill()
for i in range(n):
    turtle.forward(a)
    turtle.dot()
    turtle.left(360/n*m)
turtle.end_fill()

turtle.done()