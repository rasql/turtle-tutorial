# square with for loop
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    turtle.write(i, font=(None, '18'))
    turtle.dot()

turtle.done()