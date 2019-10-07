from algorithms.cg import CG
import tkinter as tk


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
        self.house.add_command(label='Escala Local', command=None)
        self.house.add_command(label='Escala Global', command=None)
        self.house.add_command(label='Translação', command=None)
        self.house.add_command(label='Rotação', command=None)
        self.house.add_command(label='Cisalhamento', command=None)
        self.house.add_command(label='Projeção Cavaleira', command=None)
        self.cs.add_command(label='Nova Janela', command = None)

        #adiciona os itens de menu ao menubar
        self.menu.add_cascade(label='Linha', menu=self.line)
        self.menu.add_cascade(label='Circunferência', menu=self.circ)
        self.menu.add_cascade(label='Casa', menu=self.house)
        self.menu.add_cascade(label='Cohen-Sutherland', menu=self.cs)


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
        r = ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**(1/2)
        CG.circunferencia(self.x1, self.y1, r, self.canvas)


    def call_draw_line(self):
        if self.canvas:
            self.canvas.delete('all')
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#000000")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_line)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_line)
        self.canvas.pack()
        

 
    def call_draw_circ(self):
        if self.canvas:
            self.canvas.delete('all')
        
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#000000")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_circ)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_circ)
        self.canvas.pack()
    
    

    def call_draw_house(self):
        if self.canvas:
            self.canvas.delete('all')
        
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#000000")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_house)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_house)
        self.canvas.pack()


def main():
    
    root = tk.Tk()
    root.title('Trabalho de Computação Gráfica')
    App(root)
    root.attributes('-zoomed', True)
    root.mainloop()



main()


