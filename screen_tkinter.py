#coding utf-8
from tkinter import *

class Screen:
    
    def __init__(self, root):
        self.master = root
        self.master.title('Trabalho de Computação Gráfica')
        self.menu = Menu(self.master)
        self.line = Menu(self.menu)
        self.line.add_command('New', command=draw_line)
        self.circ = Menu(self.menu)
        self.circ.add_command('New', command=draw_circ)
        self.line = Menu(self.menu)
        self.object.add_command('New', command=draw_object)
        self.menu.add_cascade(label='Line', menu=self.line)
        self.menu.add_cascade(label='Circunferência', menu=self.circ)
        self.menu.add_cascade(label='Objeto', menu=self.object)
        

    
        
root = Tk()
gui = Screen(root)
root.mainloop()