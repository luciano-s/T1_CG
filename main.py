from algorithms.cg import CG
import tkinter as tk
from tests.cs_class import *
from math import floor


class App():

    def __init__(self, master=None):
        self.canvas = None
        #passa o master Tk()
        self.master = master
        
        #define o menubar
        self.menu = tk.Menu(self.master) 
        self.master.config(menu=self.menu)

        #define os itens do menu bar
        self.line = tk.Menu(self.menu)
        self.circ = tk.Menu(self.menu)
        self.house = tk.Menu(self.menu)
        self.cs = tk.Menu(self.menu)

        #adiciona os elementos aos itens de menu
        self.line.add_command(label='Novo', command=self.call_draw_line)
        self.circ.add_command(label='Novo', command=self.call_draw_circ)
        self.house.add_command(label='Novo', command=self.call_draw_house)
        self.house.add_command(label='Escala Local', command=None)
        self.house.add_command(label='Escala Global', command=None)
        self.house.add_command(label='Translação', command=None)
        self.house.add_command(label='Rotação', command=None)
        self.house.add_command(label='Cisalhamento', command=None)
        self.house.add_command(label='Projeção Cavaleira', command=None)
        self.cs.add_command(label='Nova Janela', command = self.call_cohen_sutherland)
        
        #adiciona os itens de menu ao menubar
        self.menu.add_cascade(label='Linha', menu=self.line)
        self.menu.add_cascade(label='Circunferência', menu=self.circ)
        self.menu.add_cascade(label='Casa', menu=self.house)
        self.menu.add_cascade(label='Cohen-Sutherland', menu=self.cs)


# ----------INIÍCIO MÉTODOS DE MONITORAMENTO DE EVENTOS DE MOUSE-------------- #

    def mouse_click_line(self, event):
       
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x1 = event.x
        self.y1 = event.y
        
    
    def mouse_release_line(self, event):
        
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x2 = event.x
        self.y2 = event.y
        CG.line_breasenham(self.x1, self.y1, self.x2, self.y2, self.canvas)

    def mouse_click_circ(self, event):
       
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x1 = event.x
        self.y1 = event.y
        
    
    def mouse_release_circ(self, event):
        
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x2 = event.x
        self.y2 = event.y
        
        # input()
        r = floor(((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**(1/2))
        CG.circunferencia(self.x1, self.y1, r, self.canvas)


    
# ----------FIM MÉTODOS DE MONITORAMENTO DE EVENTOS DE MOUSE-------------- #


# ----------INÍCIO MÉTODOS DE CHAMADA DOS MÉTODOS DA CLASSE CG-------------- #


    def call_draw_line(self):
        if self.canvas:
            self.canvas.delete('all')
            self.canvas = None
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#ffffff")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_line)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_line)
        

    def call_draw_circ(self):
        if self.canvas:
            self.canvas.delete('all')
            self.canvas = None

        
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#ffffff")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_circ)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_circ)
        
    
    def call_cohen_sutherland(self):
        if self.canvas:
            self.canvas.delete('all')
            self.canvas = None
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#ffffff")
        self.canvas.grid(row=0, column=0)
        
        a = CS(self.canvas)
        self.canvas.bind("<Button-1>", a.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", a.mouse_release)


    def call_draw_house(self):
        if self.canvas:
            self.canvas.delete('all')
            self.canvas = None
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#000000")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_house)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_house)
        
        
# ----------FIM MÉTODOS DE CHAMADA DOS MÉTODOS DA CLASSE CG-------------- #

def main():
    
    root = tk.Tk()
    root.title('Trabalho de Computação Gráfica')
    App(root)
    root.attributes('-zoomed', True)
    root.mainloop()



main()


