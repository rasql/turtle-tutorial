# draw a flower
import turtle

def petal():
    turtle.begin_fill()
    turtle.circle(50, 90)
    turtle.left(90)
    turtle.circle(50, 90)
    turtle.end_fill()
    turtle.left(18)
    
def flower():
    petal()
    petal()
    petal()
    petal()
    petal()

turtle.width(2)
turtle.fillcolor('violet')
flower()
turtle.goto(80, 20)
flower()

turtle.done()