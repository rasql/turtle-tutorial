# welcome to EPFL
import turtle

turtle.color('red', 'green')
turtle.shape('turtle')
turtle.speed(1)

turtle.write('EPFL', font=(None, 64))
turtle.goto(0, -50)

def square():
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()

turtle.fillcolor('red')
for i in range(5):
    square()
    turtle.forward(60)    

turtle.done()