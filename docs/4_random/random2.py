# random direction
import turtle
import random

turtle.dot()
for i in range(100):
    angle = random.randint(-90, 90)
    turtle.forward(20)
    turtle.left(angle)
    turtle.dot()

turtle.done()