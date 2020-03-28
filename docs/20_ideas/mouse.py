# go to mouse click position
from turtle import *
import shortcuts

shape('turtle')
color('red', 'white')
speed(1)
title('SPS - Service de Promotion des Sciences - EPFL')
title('EPFL SPS - Les sciences à la maison')
bgpic('EPFL.png')
bgcolor('hotpink')

def click(x, y):
    angle = towards(x, y)
    setheading(angle)
    goto(x, y)
    dot()
    write(f'({int(x)}, {int(y)})', font=(None, 18))

onscreenclick(click)

done()
