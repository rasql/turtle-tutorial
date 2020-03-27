# draw a parallelogram
from turtle import *

a = 200
b = 150
angle = 60

forward(a)
left(angle)
forward(b)
left(180-angle)
forward(a)
left(angle)
forward(b)
left(180-angle)

done()
