# draw a tree
from turtle import *

d = 0.6         # decreasing factor
alpha = 45      # turning angle
l = 100         # initial length

def tree(a):
    if a < 10:
        return
    else:
        forward(a)
        left(alpha)
        tree(a * d)
        right(2 * alpha)
        tree(a * d)
        left(alpha)
        backward(a)

left(90)
backward(l)
tree(l)

done()
