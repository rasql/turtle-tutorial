# controlling two turtles
from turtle import *

alice = Turtle()
bob = Turtle()

alice.color('red')
bob.color('blue')

onkey(lambda: alice.forward(30), 'w')
onkey(lambda: alice.backward(30), 's')
onkey(lambda: alice.left(30), 'a')
onkey(lambda: alice.right(30), 'd')

onkey(lambda: bob.forward(30), 'Up')
onkey(lambda: bob.backward(30), 'Down')
onkey(lambda: bob.left(30), 'Left')
onkey(lambda: bob.right(30), 'Right')

listen()
done()
