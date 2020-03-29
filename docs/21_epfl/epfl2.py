# EPFL campus tour
# https://www.epfl.ch/about/
# https://www.epfl.ch/about/wp-content/uploads/2020/01/EPFL-vue-aerienne-1536x864.jpg
from turtle import *

def click(x, y):
    print(x, y)

bgpic('EPFL_campus.gif')
setup(1000, 700)
onscreenclick(click)

speed(1)
width(5)
d = 30

write('Start', font=(None, 48))
dot(d)

goto(-20, -140)
dot(d)
write('Rolex Learning Center', font=(None, 48))

goto(-350, -90)
dot(d)
write('ArtLab', font=(None, 48))

goto(-123, 177)
dot(d)
write('Mechanical Engineering', font=(None, 48))

goto(-315, 290)
dot(d)
write('Esplanade', font=(None, 48))

done()