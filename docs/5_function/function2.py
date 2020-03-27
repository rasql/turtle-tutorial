# polygon function with arguments
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot()
        left(360/n)

back(200)
polygon(3, 80)

forward(150)
polygon(5, 80)

forward(200)
polygon(9, 40)

done()