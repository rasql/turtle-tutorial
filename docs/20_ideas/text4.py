# turtle shapes
from turtle import *

color('red')
shape('turtle')

shapes = ('turtle', 'arrow', 'circle', 'square', 'triangle', 'classic')

left(90)
for s in getshapes():
    shape(s)
    stamp()
    write('   '+s, font=(None, 24))
    forward(40)
hideturtle()

done()