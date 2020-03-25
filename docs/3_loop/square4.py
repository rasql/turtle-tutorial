# nested loops
import turtle

a = 20
for i in range(7):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    a += 20

turtle.done()