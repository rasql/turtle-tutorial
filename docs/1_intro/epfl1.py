# welcome to EPFL
import turtle

turtle.color('red', 'green')
turtle.shape('turtle')
turtle.speed(1)

turtle.write('EPFL', font=(None, 36))

for i in range(6):
    turtle.forward(100)
    turtle.left(60)