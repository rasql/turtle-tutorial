# drawing a star
import turtle

a = 200
n = 5
m = 2

for i in range(n):
    turtle.forward(a)
    turtle.dot()
    turtle.left(360/n*m)

turtle.done()