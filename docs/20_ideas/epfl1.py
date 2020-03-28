# turtle config file settings - EPFL
from turtle import *

color('red')
shape('turtle')
title('EPFL - Python Turtle Graphics')
setup (width=600, height=400, startx=None, starty=None)
screensize(canvwidth=400, canvheight=300, bg=None)

n = 6
for i in range(n):
    forward(100)
    left(360/n)
    dot()

done()