# special symbols (emoji do not work)
from turtle import *

color('red')
shape('turtle')

alignement = ('left', 'center', 'right')

left(90)
for a in alignement:
    write(a, align=a, font=(None, 48))
    forward(60)

done()