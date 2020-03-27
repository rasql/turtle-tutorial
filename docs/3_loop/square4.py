# nested loops
from turtle import *

a = 20
for i in range(7):
    for j in range(4):
        forward(a)
        left(90)
    a += 20

done()