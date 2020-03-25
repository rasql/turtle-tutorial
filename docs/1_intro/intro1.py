s# Needs Pillow and ghostscript installed
# https://stackoverflow.com/questions/41940945/saving-canvas-from-tkinter-to-file

import turtle
import io
from PIL import Image


def save():
    print('save image')
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file='image.eps')
    img = Image.open('image.eps')
    img.save('image.png', 'png')
    
def move():
    turtle.left(45)
    turtle.forward(50)

turtle.onkey(save, 's')
turtle.onkey(move, 'space')

turtle.forward(100)
turtle.dot()

turtle.listen()




