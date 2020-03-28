# Needs Pillow and ghostscript installed
# https://stackoverflow.com/questions/41940945/saving-canvas-from-tkinter-to-file
# https://stackoverflow.com/questions/34777676/how-to-convert-a-python-tkinter-canvas-postscript-file-to-an-image-file-readable

from turtle import *
import time
import io
from PIL import Image

class Util:
    def __init__(self):
        self.canvas = getscreen().getcanvas()
        self.images = []
        self.file_name = 'img'
        self.recording = False
        self.dt = 50
        self.n = 0

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

    def gif_start(self):
        self.recording = True
        self.gif()

    def gif_stop(self):
        self.recording = False

    def gif(self):
        self.n += 1
        if self.recording:
            ontimer(self.gif, self.dt)
            ps = self.canvas.postscript(colormode = 'color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            print(img)
            self.images.append(img)
        else:
            print('GIF start saving', self.n, 'images')
            t0 = time.time()
            self.images[0].save(self.file_name+'.gif', save_all=True, append_images=self.images[1:],
                                        optimize=True, duration=self.dt * 2, loop=0)
            t = time.time()

            print('GIF saved')
            print(f'total time = {t-t0:.1f} s')
            print(f'frames/sec = {self.n/(t-t0):.1f}')

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
        R - reset
        Q - quit

        U - pen up
        D - pen down
        T - pen toggle
        H - toggle turtle visibility
        """)
        
util = Util()
onkey(util.help, 'h')
onkey(util.save_eps, 'e')
onkey(util.save_png, 'p')
onkey(util.save_jpg, 'j')

onkey(lambda : left(30), 'Left')
onkey(lambda : right(30), 'Right')
onkey(lambda : forward(30), 'Up')
onkey(lambda : backward(30), 'Down')

onkey(reset, 'r')
onkey(home, 'h')
onkey(clear, 'c')
onkey(bye, 'q')

onkey(up, 'u')
onkey(down, 'd')
onkey(lambda : up() if isdown() else down(), 't')
onkey(lambda : hideturtle() if isvisible() else showturtle(), 'v')

listen()

def draw():
    clear()
    n = 6
    write('EPFL', font=('Arial', 36, 'bold'))
    for i in range(n): 
        forward(100)
        dot()
        left(360/n)

def record():
    util.gif_start()
    draw()
    util.gif_stop()

onkey(draw, 'd')
onkey(record, 'r')

if __name__ == '__main__':
    
    w, h = 300, 300
    x, y = -100, -50
    setup(w, h)
    # screensize(w-20, h-20)
    # setworldcoordinates(x, y, x+w, y+h)

    up()
    goto(-60, -80)
    down()

    shape('turtle')
    color('red', 'white')
    speed(1)

    done()




