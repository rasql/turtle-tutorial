# controlling two turtles
import turtle

alice = turtle.Turtle()
bob = turtle.Turtle()

alice.color('red')
bob.color('blue')

turtle.onkey(lambda: alice.forward(30), 'w')
turtle.onkey(lambda: alice.backward(30), 's')
turtle.onkey(lambda: alice.left(30), 'a')
turtle.onkey(lambda: alice.right(30), 'd')

turtle.onkey(lambda: bob.forward(30), 'Up')
turtle.onkey(lambda: bob.backward(30), 'Down')
turtle.onkey(lambda: bob.left(30), 'Left')
turtle.onkey(lambda: bob.right(30), 'Right')

turtle.listen()
turtle.done()
