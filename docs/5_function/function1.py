# polygon function without arguments
import turtle
import random

def hexagon():
    for i in range(6):
        turtle.forward(30)
        turtle.left(60)

for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    turtle.goto(x, y)
    hexagon()

turtle.done()