# random color
from turtle import *
import random

colors = ('red', 'blue', 'green', 'violet', 'yellow', 'cyan', 
    'orange', 'magenta')


dot()
for i in range(15):
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    color = random.choice(colors)
    pencolor(color)
    goto(x, y)
    dot(40)

done()
    