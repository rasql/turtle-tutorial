# drawing a star
from turtle import *

a = 200
n = 11
m = 4

begin_fill()
for i in range(n):
    forward(a)
    dot()
    left(360/n*m)
end_fill()

done()