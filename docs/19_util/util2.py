from turtle import *

turtle.setup (width=300, height=300)
turtle.shape('turtle')
turtle.color("red", "green")
turtle.goto(-50, -50)

n = 5
for i in range(n):
    turtle.forward(100)
    turtle.left(360/n)

turtle.done()