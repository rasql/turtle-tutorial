# multiple nested polygons
from turtle import *

for n in range(3, 7):
    for i in range(n):
        forward(100)
        dot()
        left(360/n)

done()