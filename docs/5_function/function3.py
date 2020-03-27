# star function with 4 arguments
from turtle import *

def star(n, m, a, color):
    fillcolor(color)
    begin_fill()
    for i in range(n):
        forward(a)
        dot()
        left(360/n*m)
    end_fill()

back(200)
star(5, 2, 100, 'red')

forward(150)
star(7, 3, 120, 'blue')

forward(160)
star(11, 6, 120, 'yellow')

done()