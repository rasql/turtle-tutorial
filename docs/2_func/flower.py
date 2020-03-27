# draw a flower
from turtle import *

def petal():
    begin_fill()
    circle(50, 90)
    left(90)
    circle(50, 90)
    end_fill()
    left(18)
    
def flower():
    petal()
    petal()
    petal()
    petal()
    petal()

width(2)
fillcolor('violet')
flower()
goto(80, 20)
flower()

done()