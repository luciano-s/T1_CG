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
        
        draw_line(self.x1, self.y1, self.x2, self.y2, self.canvas)
        
    def get_point1(self):
        return self.x1, self.y1
    
    def get_point2(self):
        return self.x2, self.y2

    def get_root(self):
        return self.root

def draw_line(x0, y0, x1, y1, canvas):
    #desenha retas no octante 8
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    eps = 0
    
    if (dy < dx):
        if x0 < x1: # caso em que o x inicial é menor que o x final
            if y0 < y1: # caso em que o y inicial é menor que o y final
                y = y0
                for x in range(x0, x1+1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    eps += dy
                    if (2*eps >= dx):   
                        y +=1
                        eps -= dx
            else: #y1 <= y0 caso em que o y final é menor que o y inicial
                y = y0
                for x in range(x0, x1+1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    eps += dy
                    if (2*eps >= dx):   
                        y -=1
                        eps -= dx
    else: # caso em que o x final é menor que o inicial
        if y0 < y1: # caso em que o y inicial é menor que o y final
            y = y0
            for x in range(x1, x0):
                canvas.create_line(x, y, x+1, y+1, fill='white')
                eps += dy
                if (2*eps >= dx):   
                    y +=1
                    eps -= dx
            else: #y1 <= y0 caso em que o y final é menor que o y inicial
                y = y0
                for x in range(x0, x1, -1):
                    canvas.create_line(x, y, x-1, y-1, fill='white')
                    eps += dy
                    if (2*eps >= dx):   
                        y -=1
                        eps -= dx



def set_octant(i, j, o):
    
    if o==1:
        return i, j
    if o ==2:
        return j, i
    if o ==3:
        return -j, i
    if o==4:
        return -i, j
    if o==5:
        return -i, -j
    if o==6:
        return j, -i
    if o==7:
        return i, -j
    


C = Callbacks()

