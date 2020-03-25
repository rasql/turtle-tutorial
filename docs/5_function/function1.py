# polygon function without arguments
import turtle
import random

def polygon():
    for i in range(6):
        turtle.forward(30)
        turtle.left(60)

for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    turtle.goto(x, y)
    polygon()
    turtle.write(i, font=(None, 48))

turtle.done()