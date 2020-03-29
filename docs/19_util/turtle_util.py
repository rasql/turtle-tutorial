# Needs Pillow and ghostscript installed
# https://stackoverflow.com/questions/41940945/saving-canvas-from-tkinter-to-file
# https://stackoverflow.com/questions/34777676/how-to-convert-a-python-tkinter-canvas-postscript-file-to-an-image-file-readable

from turtle import *
import io, os, sys, time
from PIL import Image

class Util:
    def __init__(self):
        self.canvas = getscreen().getcanvas()
        
        module = sys.modules['__main__']
        self.path, ext = os.path.splitext(module.__file__)
        print('path', self.path)
        
        self.images = []
        self.recording = False
        self.dt = 50
        self.n = 0
        self.id = None
        self.p0 = None

        self.canvas.bind('<Button-1>', self.start)
        self.canvas.bind('<B1-Motion>', self.move)
        self.canvas.bind('<e>', lambda e: self.save_eps())
        self.canvas.bind('<j>', lambda e: self.save_jpg())
        self.canvas.bind('<p>', lambda e: self.save_png())
        self.canvas.bind('<g>', lambda e: self.save_gif())

        self.canvas.bind('<Return>', self.cb)

    def cb(self, event=None):
        print(event)

    def start(self, event=None):
        self.win_p0 = (event.x, event.y)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.p0 = (x, y)
        if self.id == None:
            self.id = self.canvas.create_rectangle(*self.p0, *self.p0)
        else:
            self.canvas.coords(self.id, *self.p0, *self.p0)

    def move(self, event=None):
        self.win_p1 = (event.x, event.y)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.p1 = (x, y)
        self.canvas.coords(self.id, *self.p0, *self.p1)

        # region to crop
        self.box = (self.win_p0[0]+1, self.win_p0[1]+2, event.x-1, event.y)

    def save_ps(self):
        print('save PostScript')
        self.canvas.postscript(file=self.path + '.ps')

    def save_eps(self):
        print('save EPS')
        self.canvas.postscript(file=self.path + '.eps')

    def save_jpg(self):
        print('save JPG')
        ps = self.canvas.postscript(colormode = 'color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        region = img.crop(self.box)
        region.save(self.path + '.jpg')

    def save_png(self):
        print('save PNG')
        ps = self.canvas.postscript(colormode = 'color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        region = img.crop(self.box)
        region.save(self.path + '.png')

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
            # print(img)
            self.images.append(img)
       
    def save_gif(self):
        print('GIF start saving', self.n, 'images')
        t0 = time.time()
        self.images2 = []
        for img in self.images:
            region = img.crop(self.box)
            self.images2.append(region)

        self.images2[0].save(self.path+'.gif', save_all=True, append_images=self.images2[1:],
                                        optimize=True, duration=self.dt * 2, loop=0)
        t = time.time()

        print('GIF saved')
        print(f'total time = {t-t0:.1f} s')
        print(f'frames/sec = {self.n/(t-t0):.1f}')


def help():
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
    V - toggle turtle visibility
    """)

onkey(lambda : left(30), 'Left')
onkey(lambda : right(30), 'Right')
onkey(lambda : forward(30), 'Up')
onkey(lambda : backward(30), 'Down')

onkey(help, 'h')
onkey(reset, 'r')
# onkey(home, 'h')
onkey(clear, 'c')
onkey(bye, 'q')

onkey(up, 'u')
onkey(down, 'd')
onkey(lambda : up() if isdown() else down(), 't')
onkey(lambda : hideturtle() if isvisible() else showturtle(), 'v')

listen()

util = Util()
util.gif_start()

def done():
    util.gif_stop()
    mainloop()

if __name__ == '__main__':
    
    n = 6
    for i in range(n):
        forward(100)
        dot()
        left(360/n)

    done()