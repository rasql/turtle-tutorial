# virus
from turtle import *

def virus(d):
    for i in range(18):
        forward(d)
        left(80)
        forward(d)
        dot()
        backward(d)
        right(100)
    
virus(10)
goto(-100, 50)
virus(15)
goto(150, 100)
virus(20)

done()
