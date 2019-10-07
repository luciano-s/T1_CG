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

        self.A2 = (0,0)
        self.B2 = (0,0)
        self.C2 = (0,0)
        self.D2 = (0,0)
        self.E2 = (0,0)
        self.F2 = (0,0)
        self.G2 = (0,0)
        self.H2 = (0,0)
        self.I2 = (0,0)
        self.J2 = (0,0)

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
        x = 0
        y = r
        d = 3 - 2*r
        draw_circle(xc, yc, x, y, canvas)
        while y >= x:
            x +=1
            if d > 0:
                y -=1
                d += 4*(x-y) + 10
            else:
                d+=4*(x-y) + 6
            draw_circle(xc, yc, x, y, canvas)

    @classmethod    
    def scale_3D(cls, type='local'):
        pass

    @classmethod
    def translation_3D(cls, ponto ):
        pass
    
    
    def cavaleira(self):
        Mc = np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], 
        [ ((2)**(1/2))/2, ((2)**(1/2))/2, 0, 0], [0, 0, 0, 1] ]) 
        

        # print(self.A)
        # print(Mc)
        # self.A = (100, 100, 100, 1)
        self.A2 = np.array(self.A) * Mc
        print(f'A2 : {self.A2}')
        self.A2 = np.array(self.A2)
        print(f'A2 : {self.A2[:1]}')
        input()
        self.B2 = np.array(self.B) * Mc
        self.B2 = self.B2[:1]
        self.C2 = np.array(self.C) * Mc
        self.C2 = self.C2[:1]
        self.D2 = np.array(self.D) * Mc
        self.D2 = self.D2[:1]
        self.E2 = np.array(self.E) * Mc
        self.E2 = self.E2[:1]
        self.F2 = np.array(self.F) * Mc
        self.F2 = self.F2[:1]
        self.G2 = np.array(self.G) * Mc
        self.G2 = self.G2[:1]
        self.H2 = np.array(self.H) * Mc
        self.H2 = self.H2[:1]
        self.I2 = np.array(self.I) * Mc
        self.I2 = self.I2[:1]
        self.J2 = np.array(self.J) * Mc
        self.J2 = self.J2[:1]
                
        for key in self.figura.keys():
            if 2 < len(self.figura[key]):

                cont = 2
                while cont < len(self.figura[key]):
                    self.figura[self.figura[key][cont]]
                    print(self.figura[self.figura[key][cont]])
                    print(self.figura[key][1])
                    print(self.figura[self.figura[key][cont]][1])
                    # print(f'x0: {x0}, y0:{y1}, x1:{x1}, y1:{y1}')
                    # canvas.create_line(x0, y0, x1, y1, fill='white')
                    cont+=1
                    print(cont)
                    input()
        
        # canvas.create_line(A2[0], A2[1], P2, fill='white')

        

    @classmethod
    def rotation_3D(cls):
        pass
        

    @classmethod
    def shearing_3D(cls):
        pass

    
def main():
    a = CG()
    a.cavaleira()
main()