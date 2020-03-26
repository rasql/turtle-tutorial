# numeric input
import turtle

a = turtle.numinput('Rectangle', 'largeur')
b = turtle.numinput('Rectangle', 'hauteur')

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)

turtle.done()
