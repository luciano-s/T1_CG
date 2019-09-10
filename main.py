from cg import CG
import tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None):
        self.master = master
        # self.itens = itens
        self.menu = None
        # self.pack()
        self.create_window()
    
    def call_draw_line(self):
        print('Call the drawing_line screen')
 
    def call_draw_circ(self):
        print('Call the drawing_circumference screen')
    
    def call_draw_house(self):
        print('Call the drawing_house screen')
    def create_window(self):
        self.menu = tk.Menu(self.master) 
        self.master.config(menu=self.menu)
        
        line = tk.Menu(self.menu)
        circ = tk.Menu(self.menu)
        house = tk.Menu(self.menu)

        line.add_command(label='New', command=self.call_draw_line)
        circ.add_command(label='New', command=self.call_draw_circ)
        house.add_command(label='New', command=self.call_draw_house)

        self.menu.add_cascade(label='Line', menu=line)
        self.menu.add_cascade(label='Circumference', menu=circ)
        self.menu.add_cascade(label='House', menu=house)


        
       
        


class Controller:
    
    @classmethod
    def create_window(cls):
        window = tk.Tk()
        window.minsize(350, 300)
        app = App(window)
        app.create_window()
        window.mainloop()

def main():
    itens = ['Linha', 'Circunferência', 'Objeto']
    Controller.create_window()
    
main()



