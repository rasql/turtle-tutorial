# EPFL logo
from turtle import *

lines = ('EPFL', 'Python', 'Turtle', 'Graphics')
speed(1)

begin_fill()
for i in range(2):
    left(90)
    forward(18)
    left(90)
    forward(21)
    
end_fill()

forward(20)
right(90)

pencolor('black')
forward(6)

for s in lines:
    write(s, font=('Arial', 30))
    forward(36)

pencolor('red')
done()