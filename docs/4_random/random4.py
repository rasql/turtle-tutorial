# random color
import turtle
import random

colors = ('red', 'blue', 'green', 'violet', 'yellow', 'cyan', 
    'orange', 'magenta')


turtle.dot()
for i in range(15):
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    color = random.choice(colors)
    turtle.pencolor(color)
    turtle.goto(x, y)
    turtle.dot(40)

turtle.done()
    