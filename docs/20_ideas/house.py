# draw a house
from turtle import *

shape('turtle')
color('red', 'white')
title('SPS - Service de Promotion des Sciences - EPFL')
title('EPFL SPS - Service de Promotion des Sciences - EPFL')
bgpic('EPFL.png')
bgcolor('hotpink')

def click(x, y):
    
    goto(x, y)
    write(f'x={x}, y={y}', font=(None, 18))

onscreenclick(click)

forward(141)
left(90)
forward(100)
left(45)
forward(100)
left(90)
forward(100)
left(45)
forward(100)

done()
