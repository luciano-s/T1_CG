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
        self.init_widgets()
        self.root.mainloop()


    def init_widgets(self):
        menu  = Menu(self.root)
        line  = Menu(menu)
        circ  = Menu(menu)
        house = Menu(menu)
        line.add_command('New', command=draw_line)
        circ.add_command('New', command=draw_circ)
        house.add_command('New', command=draw_house)


    def draw_circ():
        pass


    def draw_house():
        pass


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

def draw_object(points_list, canvas):
    # [(x0_0, y0_0, x1_0, y1_0), (x0_1, y0_1, x1_1, y1_1), ...]
    # formato da lista de pontos ^
        for points in points_list:
            x0, y0, x1, y1 = points
            draw_line(x0, y0, x1, y1, canvas)

def draw_line(x0, y0, x1, y1, canvas):
    #desenha retas no octante 8
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    eps = 0
    d = 0
    if (dy < dx): #x cresce mais rápido do que y
        if x0 < x1: #esquerda->direita
        
            if y0 < y1: #cima->baixo
            #octante 1
                y = y0
                for x in range(x0, x1+1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if d < 0:
                        d += dy
                        
                    else:
                        d += dy-dx
                        y +=1
            else: #baixo->cima
            #octante 8
                y = y0
                for x in range(x0, x1+1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if d < 0:
                        d+=dy

                    else:
                        d+= dy-dx
                        y-=1
        else: #direita->esquerda
            if y0 < y1: #cima->baixo
            #octante 4
                y = y0
                

                for x in range(x0, x1, -1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if d < 0:
                        d+=dy

                    else:
                        d+= dy-dx
                        y+=1
            else: #baixo->cima
            #octante 5
                y = y0
                for x in range(x0, x1, -1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if d < 0:
                        d+=dy

                    else:
                        d+= dy-dx
                        y-=1
    
    else: #y cresce mais rapido
        if y0 < y1:
            #cima -> baixo
            if x0 < x1:
                #esquerda->direita
                #octeto 2
                x = x0
                for y in range(y0, y1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if 0 < d:
                        d -= dx
                    else:
                        d += dy-dx  
                        x+=1
            else:
                #direita->esquerda
                #octeto 3
                x = x0
                for y in range(y0, y1+1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if 0 < d:
                        d-= dx
                    else:
                        d+= dy-dx
                        x-=1

        else:
            if x0 < x1:
                #esquerda->direita
                #octeto 7
                x = x0
                for y in range(y0, y1, -1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if 0 < d:
                        d-= dx
                    else:
                        d+= dy-dx
                        x+=1                    
            else:
                #direita->esquerda
                #octeto 6
                x = x0
                for y in range(y0, y1, -1):
                    canvas.create_line(x, y, x+1, y+1, fill='white')
                    if 0 < d:
                        d-= dx
                    else:
                        d+= dy-dx
                        x-=1                    




C = Callbacks()

