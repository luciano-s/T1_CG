from algorithms.cg import CG
import tkinter as tk
from tests.cs_class import *
from math import floor


class App():

    def __init__(self, master=None):
        self.canvas = None
        #passa o master Tk()
        self.master = master
        self.casa = CG()
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
        self.house.add_command(label='Translação', command=self.dialog_translacao)
        self.house.add_command(label='Rotação', command=None)
        self.house.add_command(label='Cisalhamento', command=None)
        self.house.add_command(label='Projeção Cavaleira', command=self.call_cavaleira)
        

        self.cs.add_command(label='Nova Janela', command = self.call_cohen_sutherland)
        
        #adiciona os itens de menu ao menubar
        self.menu.add_cascade(label='Linha', menu=self.line)
        self.menu.add_cascade(label='Circunferência', menu=self.circ)
        self.menu.add_cascade(label='Casa', menu=self.house)
        self.menu.add_cascade(label='Cohen-Sutherland', menu=self.cs)

        self.dialog_master = tk.Toplevel(self.master)
        
        
        self.dialog_master.geometry('350x100+%d+%d'% 
        (self.master.winfo_screenwidth()/2,self.master.winfo_screenheight()/2))
        self.button_set_translation = Button(self.dialog_master, text="OK", command=self.dialog_get_data)
        self.button_set_translation.grid(row=10, column=1, sticky=W)
        
        tk.Label(self.dialog_master, text="Deslocamento x:").grid(row=0, sticky=W)
        tk.Label(self.dialog_master, text="Deslocamento y:").grid(row=1, sticky=W)
        tk.Label(self.dialog_master, text="Deslocamento z:").grid(row=2, sticky=W)
        
        
        self.value_translation_x = tk.Entry(self.dialog_master)
        self.value_translation_x.grid(row=0, column=1)
        self.value_translation_y = tk.Entry(self.dialog_master)
        self.value_translation_y.grid(row=1, column=1)
        self.value_translation_z = tk.Entry(self.dialog_master)
        self.value_translation_z.grid(row=2, column=1)

        self.select_x_axis = tk.BooleanVar()
        self.select_y_axis = tk.BooleanVar()
        self.select_z_axis = tk.BooleanVar()
        
        self.check_x = tk.Checkbutton(self.dialog_master, variable=self.select_x_axis, onvalue=True, offvalue=False,
         text="X")
        self.check_x.grid(row=0, column=2 , sticky=W)
        
        self.check_y = tk.Checkbutton(self.dialog_master, variable=self.select_y_axis, onvalue=True, offvalue=False,
         text="Y")
        self.check_y.grid(row=1, column=2 , sticky=W)

        self.check_z = tk.Checkbutton(self.dialog_master, variable=self.select_z_axis, onvalue=True, offvalue=False,
         text="Z")
        self.check_z.grid(row=2, column=2 , sticky=W)
        
        
        

    
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

# ----------INÍCIO MÉTODOS DE DIALOG-------------- #

    def dialog_get_data(self):
        status_x = self.select_x_axis.get()
        status_y = self.select_y_axis.get()
        status_z = self.select_z_axis.get()
        distance_translation_x = self.value_translation_x.get()
        distance_translation_y = self.value_translation_y.get()
        distance_translation_z = self.value_translation_z.get()
        
        if status_x and status_y and status_z:
            # passa os tres
            self.call_translacao(x=True, y=True, z=True,translacao=
            [distance_translation_x,distance_translation_y,distance_translation_z])

        elif status_x and status_y:
            # passa os dois
            self.call_translacao(x=True, y=True,translacao=
            [distance_translation_x, distance_translation_y])

        elif status_x and status_z:
            # passa os dois
            self.call_translacao(x=True,z=True
            [distance_translation_x, distance_translation_z])

        elif status_z and status_y:
            # passa os dois
            self.call_translacao(y=True, z=True,translacao=
            [distance_translation_y, distance_translation_z])
        elif status_x:
            # passa o x
            self.call_translacao(x=True, translacao=
            [distance_translation_x])
        elif status_y:
            self.call_translacao(y=True, translacao=
            [distance_translation_y])
        elif status_z:
            self.call_translacao(z=True, translacao=
            [distance_translation_z])

        
        
        

        
    def dialog_translacao(self):
        self.dialog_master.lift()
        self.dialog_master.mainloop()
        



# ----------FIM MÉTODOS DE DIALOG-------------- #


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
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#ffffff")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click_house)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release_house)
    
    def call_cavaleira(self):
        if self.canvas:
            self.canvas.delete('all')
            self.canvas = None
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#ffffff")
        self.canvas.grid(row=0, column=0)
        
        self.casa.projecao = 'cav'
        print(self.casa)
        CG.call_projecao(self.casa, self.canvas)
        print(self.casa.projecao)
    

    def call_translacao(self, x=None,y=None, z=None, translacao=[]):
        if self.canvas:
            self.canvas.delete('all')
            self.canvas = None
        self.canvas = tk.Canvas(self.master, height=2000, width=2000, background="#ffffff")
        self.canvas.grid(row=0, column=0)
        if x==y==z!=None:
            # passa x  y z
            self.casa.translacao_3D('x', int(translacao[0]), self.canvas, False)
            self.casa.translacao_3D('y', int(translacao[1]), self.canvas, False)
            self.casa.translacao_3D('z', int(translacao[2]), self.canvas, True)
            
        elif x==y!=None:
            # passa x e y
            self.casa.translacao_3D('x', int(translacao[0]), self.canvas, False)
            self.casa.translacao_3D('y', int(translacao[1]), self.canvas, True)
            
            
        elif x==z!=None:
            # passa x e z
            self.casa.translacao_3D('x', int(translacao[0]), self.canvas, False)
            self.casa.translacao_3D('z', int(translacao[1]), self.canvas, True)
            
        elif y==z!=None:
            # passa y e z
            self.casa.translacao_3D('y', int(translacao[0]), self.canvas, False)
            self.casa.translacao_3D('z', int(translacao[1]), self.canvas, True)
            pass
        elif x!= None:
            # passa x
            self.casa.translacao_3D('x', int(translacao[0]), self.canvas, True)

        elif y!= None:
            # passa y
            self.casa.translacao_3D('y', int(translacao[0]), self.canvas, True)
            
        elif z!= None:
            # passa z
            self.casa.translacao_3D('z', int(translacao[0]), self.canvas, True)
            

        

        
# ----------FIM MÉTODOS DE CHAMADA DOS MÉTODOS DA CLASSE CG-------------- #

def main():
    
    root = tk.Tk()
    root.geometry('%dx%d+%d+%d'% (200, 300, root.winfo_screenheight()/2, root.winfo_screenwidth()/2))
    root.title('Trabalho de Computação Gráfica')
    App(root)
    root.attributes('-zoomed', True)
    root.mainloop()



main()



