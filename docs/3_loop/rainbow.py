# draw a rainbow
import turtle

d = 10
r = 60
colors = ('red', 'orange', 'yellow', 'lightgreen', 'lightblue', 'violet')

turtle.pensize(d)
turtle.left(90)

for color in colors:
    turtle.pencolor(color)
    turtle.circle(r, 180)
    turtle.left(90)
    turtle.up()
    turtle.forward(2*r + d)
    turtle.down()
    turtle.left(90)
    r += d

turtle.write('rain bow', font=(None, 36))
turtle.done()
