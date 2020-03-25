# virus
import turtle

def virus(d):
    for i in range(18):
        turtle.forward(d)
        turtle.left(80)
        turtle.forward(d)
        turtle.dot()
        turtle.backward(d)
        turtle.right(100)
    
virus(10)
turtle.goto(-100, 50)
virus(15)
turtle.goto(150, 100)
virus(20)

turtle.done()
