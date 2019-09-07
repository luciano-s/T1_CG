from tkinter import *
from PIL import Image, ImageTk

def mouse_event(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

# image_name = input('Nome da imagem: ')
root = Tk()
img_name = 'tests/stalin.jpg'

imagem = ImageTk.PhotoImage(file=img_name)

w = Label(root, image=imagem)

w.bind("<Button-1>", mouse_event)
# w.pack()
w.bind('<ButtonRelease-1>', mouse_event)
w.pack()


root.mainloop()

