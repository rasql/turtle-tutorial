# Koch snowflake
from turtle import *

def koch(x):
    if x < 5:
        forward(x)
    else:
        koch(x/3)
        left(60)
        koch(x/3)
        right(120)
        koch(x/3)
        left(60)
        koch(x/3)

speed(10)
koch(300)
done()