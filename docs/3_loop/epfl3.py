# welcome to EPFL
from turtle import *

color('red', 'green')
shape('turtle')
speed(1)

write('EPFL', font=(None, 64))
goto(0, -50)

def square():
    begin_fill()
    for i in range(4):
        forward(30)
        left(90)
    end_fill()

fillcolor('red')
for i in range(5):
    square()
    forward(60)    

done()