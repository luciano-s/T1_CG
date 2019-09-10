from tkinter import *
from PIL import Image, ImageTk
# from cg import CG

class Callbacks():
    def __init__(self):
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
        self.root = Tk()
        

    def mouse_click(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x1 = event.x
        self.y1 = event.y
        
    
    def mouse_release(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x2 = event.x
        self.y2 = event.y
        draw_line(self.x1, self.y1, self.x2, self.y2, self.root)
        # print(self.get_point1(), self.get_point2())

    def get_point1(self):
        return self.x1, self.y1
    
    def get_point2(self):
        return self.x2, self.y2

    def get_root(self):
        return self.root

def draw_line(x0, y0, x1, y1, root):
    canvas = Canvas(root, width=400,height=400, background='white')
    print(x0, y0, x1, y1)
    y = y0
    for x in range(x0, x1+1):
        canvas.create_line(x, y, x, y, fill="#476042")



# image_name = input('Nome da imagem: ')
C = Callbacks()
root = C.get_root()
# img_name = 'tests/background.jpg'
# imagem = ImageTk.PhotoImage(file=img_name)
root.minsize(400, 400)
w = Label(root)

w.bind("<Button-1>", C.mouse_click)

# w.pack()
w.bind('<ButtonRelease-1>', C.mouse_release)
w.pack()

# CG.line_breasenham((x0, y0), (x1, y1), root)
root.mainloop()


