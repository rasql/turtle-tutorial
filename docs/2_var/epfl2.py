# welcome to EPFL
from turtle import *

color('red', 'green')
shape('turtle')
speed(1)

faculties = ('SB', 'ENAC', 'STI', 'IC', 'SV')


for i in range(5):
    write(faculties[i], font=(None, 36))
    forward(80)
    left(72)

done()