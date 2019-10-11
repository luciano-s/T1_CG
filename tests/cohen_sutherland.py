# Python program to implement Cohen Sutherland algorithm
# for line clipping.
from tkinter import *
# Defining region codes


class Callbacks():
    
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.coord_retangulo = []
        self.coord_linha = []
        self.retangulo = False
        self.root = Tk()
        self.canvas = Canvas(self.root, width=2000, height=2000, background='#000000')
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.canvas.pack()
        self.root.title('Cohen-Sutherland')
        self.root.mainloop()
        


    def mouse_click(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x1 = event.x
        self.y1 = event.y
        
    
    def mouse_release(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x2 = event.x
        self.y2 = event.y
        
        if self.retangulo == False:
            print('entrou')
            self.canvas.create_rectangle(
                min([self.x1,self.x2]), min(self.y1, self.y2),
                max([self.x1,self.x2]), max(self.y1, self.y2) , outline='white')

            cohenSutherlandClip(self.x1, self.y1,self.x2, self.y2, self.retangulo,
            self.canvas)
            self.retangulo = True

        else:
            cohenSutherlandClip(self.x1, self.y1,self.x2, self.y2, self.retangulo,
            self.canvas)


        
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

# definir o tamanho do janela



# Function to compute region code for a point(x,y)canvas.create_rectangle(min([x1, x2]),min([y1, y2]) , 
        
def computeCode(x, y):
    code = INSIDE
    global x_max
    global y_max
    global x_min
    global y_min
    if x < x_min:	 # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:	 # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    return code


# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def cohenSutherlandClip(x1, y1, x2, y2, retangulo, canvas):
    if not retangulo:
        global x_max
        x_max = max(x2,x1)
        global y_max
        y_max = max(y2,y1)
        global x_min
        x_min = min(x1,x2)
        global y_min
        y_min = min(y1,y2)
    # Compute region codes for P1, P2
    else:
        print(f'coordenadas da janela: {x_min, y_min, x_max, y_max}')
        code1 = computeCode(x1, y1)
        code2 = computeCode(x2, y2)
        accept = False

        while True:

            # If both endpoints lie within rectangle
            if code1 == 0 and code2 == 0:
                accept = True
                # desenhar
                break

            # If both endpoints are outside rectangle
            elif (code1 & code2) != 0:
                # não desenhar
                break

            # Some segment lies within the rectangle
            else:

                # Line Needs clipping
                # At least one of the points is outside,
                # select it
                x = 1.0
                y = 1.0
                if code1 != 0:
                    code_out = code1
                else:
                    code_out = code2

                # Find intersection point
                # using formulas y = y1 + slope * (x - x1),
                # x = x1 + (1 / slope) * (y - y1)
                if code_out & TOP:

                    # point is above the clip rectangle
                    x = x1 + (x2 - x1) * \
                        (y_max - y1) / (y2 - y1)
                    y = y_max

                elif code_out & BOTTOM:

                    # point is below the clip rectangle
                    x = x1 + (x2 - x1) * \
                        (y_min - y1) / (y2 - y1)
                    y = y_min

                elif code_out & RIGHT:

                    # point is to the right of the clip rectangle
                    y = y1 + (y2 - y1) * \
                        (x_max - x1) / (x2 - x1)
                    x = x_max

                elif code_out & LEFT:

                    # point is to the left of the clip rectangle
                    y = y1 + (y2 - y1) * \
                        (x_min - x1) / (x2 - x1)
                    x = x_min

                # Now intersection point x,y is found
                # We replace point outside clipping rectangle
                # by intersection point
                if code_out == code1:
                    x1 = x
                    y1 = y
                    code1 = computeCode(x1, y1)

                else:
                    x2 = x
                    y2 = y
                    code2 = computeCode(x2, y2)

        if accept:
            print("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1, y1, x2, y2))
            canvas.create_line(x1, y1, x2, y2, fill='red')

            # Here the user can add code to display the rectangle
            # along with the accepted (portion of) lines

        else:
            print("Line rejected")


# Driver Script
# First Line segment
# P11 = (5, 5), P12 = (7, 7)
# cohenSutherlandClip(5, 5, 7, 7)

# Second Line segment
# P21 = (7, 9), P22 = (11, 4)
# cohenSutherlandClip(7, 9, 11, 4)

# Third Line segment
# P31 = (1, 5), P32 = (4, 1)
# cohenSutherlandClip(1, 5, 4, 1)
C = Callbacks()