# welcome to EPFL
import turtle

turtle.color('red', 'green')
turtle.shape('turtle')
turtle.speed(1)

faculties = ('SB', 'ENAC', 'STI', 'IC', 'SV')


for i in range(5):
    turtle.write(faculties[i], font=(None, 36))
    turtle.forward(80)
    turtle.left(72)

turtle.done()