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
        

    def get_root(self):
        return self.root

def draw_line(x0, y0, x1, y1, canvas):
    print(x0, y0, x1, y1)
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    j = y0
    erro = dy-dx
    
    if erro <= 0:
        if x0 < x1:
            if y0 <= y1:
                for i in range(x0, x1+1):
                 
                    canvas.create_line(i, j, i+1, j+1, fill='white')

                    if 0 <= erro:
                        j +=1
                        erro -= dx
                    i +=1
                    erro +=dy
            else:
                for i in range(x0, x1+1):
                    canvas.create_line(i, j, i+1, j+1, fill='white')

                    if 0 <= erro:
                        j -=1
                        erro -= dx
                    i +=1
                    erro +=dy        
        elif x1 < x0:
            if y0 <= y1:
                for i in range(x0, x1+1, -1):
                    canvas.create_line(i, j, i+1, j+1, fill='white')

                    if 0 <= erro:
                        j +=1
                        erro -= dx
                    i -=1
                    erro +=dy
            else:
                for i in range(x0, x1+1, -1):
                    canvas.create_line(i, j, i+1, j+1, fill='white')

                    if 0 <= erro:
                        j -=1
                        erro -= dx
                    i -=1
                    erro +=dy
    else:
        if x0 < x1:
            if y0 <= y1:
                for i in range(y0, y1+1):
                    canvas.create_line(j,i, j+1, i+1, fill='white')
                    if 0 <= erro:
                        j +=1
                        erro -= dy
                    i +=1
                    erro +=dx
            else:
                for i in range(y0, y1+1):
                    canvas.create_line(j, i, j+1, i+1, fill='white')

                    if 0 <= erro:
                        j -=1
                        erro -= dy
                    i +=1
                    erro +=dx        
        elif x1 < x0:
            if y0 <= y1:
                for i in range(y0, y1+1, -1):
                    canvas.create_line(j,i, j+1, i+1, fill='white')

                    if 0 <= erro:
                        j +=1
                        erro -= dy
                    i -=1
                    erro +=dx
            else:
                for i in range(y0, y1+1, -1):
                    canvas.create_line(j, i, j+1, i+1, fill='white')

                    if 0 <= erro:
                        j -=1
                        erro -= dy
                    i -=1
                    erro +=dx
                    

def start():
    C = Callbacks()

