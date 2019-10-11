from tkinter import *
import numpy as np


class CG:
    
    def __init__(self):
        self.A = (100, 100, 100, 1)
        self.B = (100, 100, 250, 1)
        self.C = (150, 100, 220, 1)
        self.D = (200, 100, 150, 1)
        self.E = (200, 100, 100, 1)
        self.F = (100, 200, 100, 1)
        self.G = (100, 200, 250, 1)
        self.H = (150, 200, 220, 1)
        self.I = (200, 200, 150, 1)
        self.J = (200, 200, 100, 1)
        self.A2 =(100, 100) 
        self.B2 =(100, 100) 
        self.C2 =(150, 100) 
        self.D2 =(200, 100) 
        self.E2 =(200, 100) 
        self.F2 =(100, 200) 
        self.G2 =(100, 200) 
        self.H2 =(150, 200) 
        self.I2 =(200, 200) 
        self.J2 =(200, 200) 
       

        self.figura = {'A':[self.A, self.A2, 'B', 'E', 'F'], 'B':[self.B, self.B2, 'C', 'D', 'G'],
        'C':[self.C, self.C2, 'D', 'H'],'D':[self.D, self.D2, 'E', 'I'], 'E':[self.E, self.E2, 'J'], 
        'F':[self.F, self.F2, 'G', 'J'],'G':[self.G, self.G2, 'H', 'I'], 'H':[self.H, self.H2, 'I'],
        'I':[self.I, self.I2, 'J'],'J':[self.J, self.J2]}

        
    @classmethod
    def line_breasenham(cls, x0, y0, x1, y1, canvas):
        dx = abs(x1-x0)
        dy = abs(y1-y0)
        d = 0
        if (dy < dx): #x cresce mais rápido do que y
            if x0 < x1: #esquerda->direita
            
                if y0 < y1: #cima->baixo
                #octante 1
                    y = y0
                    for x in range(x0, x1+1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if d < 0:
                            d += dy
                            
                        else:
                            d += dy-dx
                            y +=1
                else: #baixo->cima
                #octante 8
                    y = y0
                    for x in range(x0, x1+1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if d < 0:
                            d+=dy

                        else:
                            d+= dy-dx
                            y-=1
            else: #direita->esquerda
                if y0 < y1: #cima->baixo
                #octante 4
                    y = y0
                    

                    for x in range(x0, x1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if d < 0:
                            d+=dy

                        else:
                            d+= dy-dx
                            y+=1
                else: #baixo->cima
                #octante 5
                    y = y0
                    for x in range(x0, x1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if d < 0:
                            d+=dy

                        else:
                            d+= dy-dx
                            y-=1
        
        else: #y cresce mais rapido
            if y0 < y1:
                #cima -> baixo
                if x0 < x1:
                    #esquerda->direita
                    #octeto 2
                    x = x0
                    for y in range(y0, y1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if 0 < d:
                            d -= dx
                        else:
                            d += dy-dx  
                            x+=1
                else:
                    #direita->esquerda
                    #octeto 3
                    x = x0
                    for y in range(y0, y1+1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if 0 < d:
                            d-= dx
                        else:
                            d+= dy-dx
                            x-=1

            else:
                if x0 < x1:
                    #esquerda->direita
                    #octeto 7
                    x = x0
                    for y in range(y0, y1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if 0 < d:
                            d-= dx
                        else:
                            d+= dy-dx
                            x+=1                    
                else:
                    #direita->esquerda
                    #octeto 6
                    x = x0
                    for y in range(y0, y1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='white')
                        if 0 < d:
                            d-= dx
                        else:
                            d+= dy-dx
                            x-=1                    

        
    @classmethod
    def draw_circle(cls, xc, yc, x, y, canvas):
        canvas.create_line(xc+x, yc+y, (xc+x)+1, (yc+y)+1,fill='white') 
        canvas.create_line(xc-x, yc+y, (xc-x)+1, (yc+y)+1,fill='white') 
        canvas.create_line(xc+x, yc-y, (xc+x)+1, (yc-y)+1,fill='white') 
        canvas.create_line(xc-x, yc-y, (xc-x)+1, (yc-y)+1,fill='white') 
        canvas.create_line(xc+y, yc+x, (xc+y)+1, (yc+x)+1,fill='white') 
        canvas.create_line(xc-y, yc+x, (xc-y)+1, (yc+x)+1,fill='white') 
        canvas.create_line(xc+y, yc-x, (xc+y)+1, (yc-x)+1,fill='white') 
        canvas.create_line(xc-y, yc-x, (xc-y)+1, (yc-x)+1,fill='white')


    @classmethod
    def circunferencia(cls, xc, yc, r, canvas):
        print('entrou circunferencia')
        x = 0
        y = r
        d = 3 - 2*r
        CG.draw_circle(xc, yc, x, y, canvas)
        print(f'xc: {xc}, yc: {yc}, x: {x}, y: {y}, r: {r}, d: {d}')
        while y >= x:
            x +=1
            if d > 0:
                print(y)
                y -=1
                d += 4*(x-y) + 10
            else:
                d+=4*(x) + 6
            CG.draw_circle(xc, yc, x, y, canvas)
            print(f'xc: {xc}, yc: {yc}, x: {x}, y: {y}, r: {r}, d: {d}')

    @classmethod    
    def scale_3D(cls, type='local'):
        pass

    @classmethod
    def translation_3D(cls, ponto ):
        pass
    
    
    def cavaleira(self):
        Mc = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], 
        [ ((2)**(1/2))/2, ((2)**(1/2))/2, 0, 0], [0, 0, 0, 1] ]) 
        #

        # print(self.A)
        # print(Mc)
        # self.A = (100, 100, 100, 1)
        self.A2 = np.dot(np.array(self.A),Mc)
        self.A2 = self.A2[:2]
        # input()

        self.B2 = np.dot(np.array(self.B), Mc)
        self.B2 = self.B2[:1]
        self.C2 = np.dot(np.array(self.C), Mc)
        self.C2 = self.C2[:1]
        self.D2 = np.dot(np.array(self.D), Mc)
        self.D2 = self.D2[:1]
        self.E2 = np.dot(np.array(self.E), Mc)
        self.E2 = self.E2[:1]
        self.F2 = np.dot(np.array(self.F), Mc)
        self.F2 = self.F2[:1]
        self.G2 = np.dot(np.array(self.G), Mc)
        self.G2 = self.G2[:1]
        self.H2 = np.dot(np.array(self.H), Mc)
        self.H2 = self.H2[:1]
        self.I2 = np.dot(np.array(self.I), Mc)
        self.I2 = self.I2[:1]
        self.J2 = np.dot(np.array(self.J), Mc)
        self.J2 = self.J2[:1]
        print(f'A2: {self.A2}')


        # self.figura = {'A':[self.A, self.A2, 'B', 'E', 'F'], 'B':[self.B, self.B2, 'C', 'D', 'G'],
        # 'C':[self.C, self.C2, 'D', 'H'],'D':[self.D, self.D2, 'E', 'I'], 'E':[self.E, self.E2, 'J'], 
        # 'F':[self.F, self.F2, 'G', 'J'],'G':[self.G, self.G2, 'H', 'I'], 'H':[self.H, self.H2, 'I'],
        # 'I':[self.I, self.I2, 'J'],'J':[self.J, self.J2]}

        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.E2[0], self.E2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.F2[0], self.F2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')        
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')
        # canvas.create_line(self.A2[0], self.A2[1], self.B2[0], self.B2[1], fill='white')

        

    @classmethod
    def rotation_3D(cls):
        pass
        

    @classmethod
    def shearing_3D(cls):
        pass

    
def main():
    # root = Tk()
    canvas = Canvas(None, bg = '#000000')
    a = CG()
    a.cavaleira()

    # root.pack()
    # root.mainloop()
    # Mc = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], 
    #     [ ((2)**(1/2))/2, ((2)**(1/2))/2, 0, 0], [0, 0, 0, 1] ]) 
    

main()