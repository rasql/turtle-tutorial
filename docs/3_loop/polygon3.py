# drawing a star
from turtle import *

a = 200
n = 5
m = 2

for i in range(n):
    forward(a)
    dot()
    left(360/n*m)

done()