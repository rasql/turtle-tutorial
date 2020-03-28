from turtle import *

setup (width=300, height=300)
shape('turtle')
color("red", "green")
goto(-50, -50)

n = 5
for i in range(n):
    forward(100)
    left(360/n)

done()