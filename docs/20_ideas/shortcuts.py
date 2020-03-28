# define (key) shortcuts
from turtle import *

w = 1
def change_width():
    global w
    w = (w % 4) + 1
    width(w)

onkey(lambda : left(30), 'Left')
onkey(lambda : right(30), 'Right')
onkey(lambda : forward(30), 'Up')
onkey(lambda : backward(30), 'Down')

onkey(reset, 'r')
onkey(home, 'h')
onkey(clear, 'c')
onkey(bye, 'q')

onkey(up, 'u')
onkey(down, 'd')
onkey(lambda : up() if isdown() else down(), 't')
onkey(lambda : hideturtle() if isvisible() else showturtle(), 'v')
onkey(lambda : end_fill() if filling() else begin_fill(), 'f')
onkey(change_width, 'w')

onkey(undo, 'z')
onkey(stamp, 's')

onkey(lambda : circle(20), 'F1')
onkey(lambda : circle(40), 'F2')
onkey(lambda : circle(80), 'F3')

onkey(lambda : width(1), '1')
onkey(lambda : width(2), '2')
onkey(lambda : width(3), '3')

listen()