# random position
import turtle
import random

turtle.dot()
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    turtle.goto(x, y)
    turtle.dot()

turtle.done()
    