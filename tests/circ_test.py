# from algorithms.cg import CG
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
        self.root.title('Bresenham Círculo')
        self.root.mainloop()


    def mouse_click(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x1 = event.x
        self.y1 = event.y
        
    
    def mouse_release(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x2 = event.x
        self.y2 = event.y
        r = ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2)    
        call_circ_bresenham(self.x1, self.y1, r , self.canvas)

def draw_circle( xc, yc, x, y, canvas):
    canvas.create_line(xc+x, yc+y, (xc+x)+1, (yc+y)+1,fill='white') 
    canvas.create_line(xc-x, yc+y, (xc-x)+1, (yc+y)+1,fill='white') 
    canvas.create_line(xc+x, yc-y, (xc+x)+1, (yc-y)+1,fill='white') 
    canvas.create_line(xc-x, yc-y, (xc-x)+1, (yc-y)+1,fill='white') 
    canvas.create_line(xc+y, yc+x, (xc+y)+1, (yc+x)+1,fill='white') 
    canvas.create_line(xc-y, yc+x, (xc-y)+1, (yc+x)+1,fill='white') 
    canvas.create_line(xc+y, yc-x, (xc+y)+1, (yc-x)+1,fill='white') 
    canvas.create_line(xc-y, yc-x, (xc-y)+1, (yc-x)+1,fill='white')


def circumference_bresenham(xc, yc, r, canvas):
    d = 3-2*r
    x = 0
    y = r
    coords = []
    coords.append((xc, yc, x, y))
        
    while x < y:
        x+=1
        if 0 < d:
            y -=1
            d = d + 4* (x -y) + 10
        else:
            d = d + 4 * x + 6
            
        coords.append((xc, yc, x, y))
    return coords


def adjust_coords(coords, xc, yc):
    adjusted_coords = []
    for coord in coords:
        adjusted_coords.append( (xc, yc, coord[2]+xc, coord[3]+yc) )
    return adjusted_coords


def plot_circle(coords, canvas):
    for coord in coords:
        print(f'({coord[0]}, {coord[1]})')
        print(f'({coord[2]}, {coord[3]})')
        canvas.create_line(coord[2], coord[3], coord[2]+1, coord[3]+1, fill='white')
        
    
def circunferencia(xc, yc, r, canvas):
        x = 0
        y = r
        print(r)
        d = 3 - 2*r
        draw_circle(xc, yc, x, y, canvas)
        while y >= x:
            x +=1
            if d > 0:
                y -=1
                d = d + 4*(x-y) + 10
            else:
                d= d + 4*x + 6
            draw_circle(xc, yc, x, y, canvas)

def call_circ_bresenham(xc, yc, r, canvas):
    
    circunferencia(xc, yc, r, canvas)
    # coords = circumference_bresenham(xc-xc, yc-yc, r, canvas)
    # plot_circle(coords)
    # new_coords = adjust_coords(coords, xc, yc)
    # plot_circle(new_coords, canvas)


C = Callbacks()