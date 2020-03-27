# draw a tree
import turtle

d = 0.6         # decreasing factor
alpha = 45      # turning angle
l = 100         # initial length

def tree(a):
    if a < 10:
        return
    else:
        turtle.forward(a)
        turtle.left(alpha)
        tree(a * d)
        turtle.right(2 * alpha)
        tree(a * d)
        turtle.left(alpha)
        turtle.backward(a)

turtle.left(90)
turtle.backward(l)
tree(l)

turtle.done()
