# welcome to EPFL
from turtle import *
import random

color('red', 'green')
shape('turtle')
speed(1)

sections = ('mathématiques', 'chimie', 'physique', 'informatique', 'syscom', 'architecture', 'génie civil', 
    'environnement', 'électricité', 'mécanique', 'materiaux', 'microtechnique', 'sciences de la vie')

dot()
write('sections', font=(None, 36))

for s in sections:
    x = random.randint(-300, 200)
    y = random.randint(-150, 150)
    goto(x, y)
    dot()
    write(s, font=(None, 12))

done()