from algorithms.cg import CG
from tkinter import *

class Callbacks():
    def __init__(self):
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
        self.root = Tk()
        self.canvas = Canvas(self.root, width=2000, height=2000, background='#000000')
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.canvas.pack()
        self.root.mainloop()


    def mouse_click(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x1 = event.x
        self.y1 = event.y
        
    
    def mouse_release(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x2 = event.x
        self.y2 = event.y
        
        draw_circ(self.x1, self.y1, self.x2, self.y2, self.canvas)


def adjust_coords(coords, xc, yc):
    new_coords = []
    for coord in coords:
        new_coords.append( coord[0]+xc, coord[1]+yc, coord[2], coord[3] )
    return new_coords

def draw_circ(xc, yc, x, y, canvas):
    r = (x**2 + y**2)**(1/2)
    coord = []

    coords = CG.circumference_bresenham(xc-xc, yc-yc, r, x, y, canvas)
    new_coords = []
    new_coords = adjust_coords(coords, xc, yc)
    for coord in new_coords:
        draw_circ(coord[0], coord[1], coord[2], coord[3], canvas)

C = Callbacks()