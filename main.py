from cg import CG
import tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None, itens=None):
        super().__init__(master)
        self.master = master
        self.itens = itens
        self.pack()
        self.create_window()
    

    def say_hi(self):
        print("hi there, everyone!")


    def create_window(self):
        if self.itens==None:
            return None
        add_itens = []
        for i in self.itens:
            menu = tk.Menu(self.master)
            add_itens.append(tk.Menu(menu))
        c = 0
        for i in self.itens:
            new_item = add_itens[c]
            new_item.add_command(label='Novo')
            menu.add_cascade(label=i, menu=new_item)
            self.master.config(menu=menu)
            c+=1

class Controller():
    
    @classmethod

    def create_window(cls, itens=None):
        window = tk.Tk()
        window.minsize(250, 300)
        app = App(window, itens)
        app.create_window()
        app.mainloop()

def main():
    itens = ['Linha', 'Circunferência', 'Objeto']
    Controller.create_window(itens)
    
    
    
main()



