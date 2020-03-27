# Needs Pillow and ghostscript installed
# https://stackoverflow.com/questions/41940945/saving-canvas-from-tkinter-to-file
# https://stackoverflow.com/questions/34777676/how-to-convert-a-python-tkinter-canvas-postscript-file-to-an-image-file-readable

from turtle import *
import time
import io
from PIL import Image

class Util:
    def __init__(self):
        self.canvas = turtle.getscreen().getcanvas()
        self.images = []
        self.file_name = 'img'
        self.recording = True
        self.n = 0
        turtle.ontimer(self.gif, 10)

    def save_ps(self):
        print('save PostScript')
        self.canvas.postscript(file=self.file_name + '.ps')

    def save_eps(self):
        print('save EPS')
        self.canvas.postscript(file=self.file_name + '.eps')

    def save_jpg(self):
        print('save JPG')
        ps = self.canvas.postscript(colormode = 'color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save(self.file_name + '.jpg')

    def save_png(self):
        print('save PNG')
        ps = self.canvas.postscript(colormode = 'color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save(self.file_name + '.png')

    def gif(self):
        self.n += 1
        if self.recording:
            turtle.ontimer(self.gif, 10)
            ps = self.canvas.postscript(colormode = 'color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            self.images.append(img)
        else:
            print('GIF start', self.n, 'images')
            self.images[0].save(self.file_name+'.gif', save_all=True, append_images=self.images[1:],
                                        optimize=True, duration=10, loop=0)
            print('GIF saved')

    def help(self):
        print("""
        Press key

        H - get this help menu
        P - save PNG
        J - save JPG
        E - save EPS

        UP - move forward
        DOwN - move backward
        LEFT - turn left
        RIGHT - turn right

        C - clear
        H - home
        Q - quit
        U - pen up
        D - pen down
        """)
        

util = Util()
turtle.onkey(util.help, 'h')
turtle.onkey(util.save_eps, 'e')
turtle.onkey(util.save_png, 'p')
turtle.onkey(util.save_jpg, 'j')

turtle.onkey(lambda : turtle.left(30), 'Left')
turtle.onkey(lambda : turtle.right(30), 'Right')
turtle.onkey(lambda : turtle.forward(30), 'Up')
turtle.onkey(lambda : turtle.backward(30), 'Down')

turtle.onkey(turtle.reset, 'r')
turtle.onkey(turtle.clear, 'c')
turtle.onkey(turtle.bye, 'q')

turtle.onkey(turtle.up, 'u')
turtle.onkey(turtle.down, 'd')
turtle.listen()

if __name__ == '__main__':
    
    w, h = 300, 300
    x, y = -100, -50
    # turtle.setup(w, h)
    # turtle.screensize(w-20, h-20)
    # turtle.setworldcoordinates(x, y, x+w, y+h)
    print(util.canvas)

    turtle.shape('turtle')
    turtle.color("red", "green")

    n = 6
    for i in range(n): 
        turtle.forward(100)
        turtle.dot()
        turtle.left(360/n)

    util.recording = False

    turtle.done()




