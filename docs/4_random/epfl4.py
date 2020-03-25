# welcome to EPFL
import turtle
import random

turtle.color('red', 'green')
turtle.shape('turtle')
turtle.speed(1)

sections = ('mathématiques', 'chimie', 'physique', 'informatique', 'syscom', 'architecture', 'génie civil', 
    'environnement', 'électricité', 'mécanique', 'materiaux', 'microtechnique', 'sciences de la vie')

turtle.dot()
turtle.write('sections', font=(None, 36))

for s in sections:
    x = random.randint(-300, 200)
    y = random.randint(-150, 150)
    turtle.goto(x, y)
    turtle.dot()
    turtle.write(s, font=(None, 12))

turtle.done()