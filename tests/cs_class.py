from tkinter import *

class CS(object):
    
    def __init_(self,):
        self.INSIDE = 0  # 0000
        self.LEFT   = 1  # 0001
        self.RIGHT  = 2  # 0010
        self.BOTTOM = 4  # 0100
        self.TOP    = 8  # 1000
        self.x_max = None
        self.y_max = None
        self.self.x_min = None
        self.y_min = None
        self.retangulo = None
        self.canvas = None

    def set_canvas(self, cv):
        self.canvas = cv
    
    def set_retangulo(self, ret):
        self.retangulo = ret
    


    def cohenSutherlandClip(self, retangulo ,canvas):
        x1 = x_min
        x2 = x_max
        y1 = y_min
        y2 = y_max
        if not retangulo:
            
            self.x_max = max(x2,x1)
            self.y_max = max(y2,y1)
            self.x_min = min(x1,x2)
            self.y_min = min(y1,y2)

        # Compute region codes for P1, P2
        else:
            print(f'coordenadas da janela: {self.x_min, self.y_min, self.x_max, self.y_max}')
            
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
                    if code_out & self.TOP:

                        # point is above the clip rectangle
                        x = x1 + (x2 - x1) * \
                            (y_max - y1) / (y2 - y1)
                        y = y_max

                    elif code_out & self.BOTTOM:

                        # point is below the clip rectangle
                        x = x1 + (x2 - x1) * \
                            (y_min - y1) / (y2 - y1)
                        y = y_min

                    elif code_out & self.RIGHT:

                        # point is to the right of the clip rectangle
                        y = y1 + (y2 - y1) * \
                            (x_max - x1) / (x2 - x1)
                        x = x_max

                    elif code_out & self.LEFT:

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


    def computeCode(self, x, y):
        
        code = self.INSIDE
    
        if x < self.x_min:	 # to the left of rectangle
            code |= self.LEFT
        elif x > self.x_max:  # to the right of rectangle
            code |= self.RIGHT
        if y < self.y_min:	 # below the rectangle
            code |= self.BOTTOM
        elif y > self.y_max:  # above the rectangle
            code |= self.TOP

        return code

    def mouse_click(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x_min = event.x
        self.y_min = event.y


    def mouse_release(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x_max = event.x
        self.y_max = event.y
        if not self.retangulo:
            if self.x_max < self.x_min:
                self.x_max=self.x_min

            if self.y_max < self.y_min:
                self.y_max=self.y_min
            self.retangulo = True
        
        self.cohenSutherlandClip(self.retangulo, self.canvas)


def main():
    root = Tk()
    canvas = Canvas(root, width=2000, height=2000, background = '#ffffff')
    canvas.grid(row=0, column=0)
    a = CS()
    a.set_canvas(canvas)
    canvas.bind("<Button-1>", a.mouse_click)
    canvas.bind("<ButtonRelease-1>", a.mouse_release)
    root.title('Cohen-Sutherland')
    
    root.mainloop()


main()