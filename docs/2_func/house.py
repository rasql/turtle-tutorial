# define a function
from turtle import *

def house():
    begin_fill()
    forward(141)
    left(90)
    forward(100)
    left(45)
    forward(100)
    left(90)
    forward(100)
    left(45)
    forward(100)
    left(90)
    end_fill()

width(4)
house()
goto(-100, -20)
fillcolor('yellow')
house()

done()