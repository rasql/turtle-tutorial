from turtle import *

color('red')
shape('turtle')
r = 40

circle(r)
circle(-r)
forward(100)

for i in range(4):
    forward(100)
    circle(r, 90)

goto(-100, -100)

for i in range(6):
    circle(r)
    left(60)

done()