# define a function
from turtle import *

def side():
    forward(100)
    left(90)

def square():
    side()
    side()
    side()
    side()
    forward(100)

square()
square()
square()

done()