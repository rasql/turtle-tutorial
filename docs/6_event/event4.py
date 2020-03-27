# using key events with a lambda function
import turtle

turtle.onkey(lambda: turtle.forward(30), 'Up')
turtle.onkey(lambda: turtle.backward(30), 'Down')
turtle.onkey(lambda: turtle.left(30), 'Left')
turtle.onkey(lambda: turtle.right(30), 'Right')
turtle.listen()

turtle.forward(0)
turtle.done()
