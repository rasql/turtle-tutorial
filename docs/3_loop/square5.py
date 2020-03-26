# nested loops
import turtle

for a in range(40, 160, 20):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

turtle.done()