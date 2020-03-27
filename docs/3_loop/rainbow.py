# draw a rainbow
from turtle import *

d = 10
r = 60
colors = ('red', 'orange', 'yellow', 'lightgreen', 'lightblue', 'violet')

pensize(d)
left(90)

for color in colors:
    pencolor(color)
    circle(r, 180)
    left(90)
    up()
    forward(2*r + d)
    down()
    left(90)
    r += d

write('rain bow', font=(None, 36))
done()
