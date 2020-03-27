# Needs Pillow and ghostscript installed
# https://stackoverflow.com/questions/41940945/saving-canvas-from-tkinter-to-file
import turtle
import time
import io
from PIL import Image

screen = turtle.getscreen()
canvas = screen.getcanvas()
images = []

class Util:
    def __init__(self):
        self.canvas = turtle.getscreen().getcanvas()
        self.images = []

    def save_ps(self):
        print('UTIL save PostScript')
        self.canvas.postscript(file='util_image.ps')

def save_ps():
    print('save PostScript')
    canvas.postscript(file='image.ps')

def save_eps():
    print('save EPS')
    canvas.postscript(file='image.eps')

def save_jpg():
    # https://stackoverflow.com/questions/34777676/how-to-convert-a-python-tkinter-canvas-postscript-file-to-an-image-file-readable
    print('save JPG')
    ps = canvas.postscript(colormode = 'color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('image.jpg')

def save():
    print('save image')
    ts = turtle.getscreen()
    ps = ts.getcanvas().postscript()
    img = Image.open(ps)
    img.save('image.png', 'png')

def save_gif():
    print('save GIF')
    
def move():
    turtle.left(45)
    turtle.forward(50)


def gif():
    t = time.time()
    # print('gif', t-t0)
    if running:
        turtle.ontimer(gif, 10)
        ps = canvas.postscript(colormode = 'color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        images.append(img)
    else:
        print('GIF start')
        images[0].save('image.gif', save_all=True, append_images=images[1:],
                                    optimize=True, duration=10, loop=0)
        print('GIF saved')
        images[-1].save('image.png', 'png')
        

util = Util()

turtle.onkey(save, 's')
turtle.onkey(util.save_ps, 'p')
turtle.onkey(save_eps, 'e')
turtle.onkey(save_gif, 'g')
turtle.onkey(save_jpg, 'j')
turtle.onkey(move, 'space')
turtle.ontimer(gif, 10)
turtle.listen()


if __name__ == '__main__':
    print('delay', turtle.delay())
    t0 = time.time()
    running = True

    n = 6
    turtle.speed(1)
    turtle.shape('turtle')
    turtle.color("red", "green")
    for i in range(n): 
        turtle.forward(100)
        turtle.dot()
        turtle.left(360/n)

    running = False
    t = time.time()
    print('t=', t-t0)

    turtle.done()




