from tkinter import *

class CG:
    
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
    def circumference_bresenham(cls, xc, yc, r,x, y, canvas):
        d = 3-2*r
        coords = []
        coords.append((xc, yc, x, y))
        CG.draw_circle(xc, yc, x, y, canvas)
        while x < y:
            x+=1
            if 0 < d:
                y -=1
                d = d + 4* (x -y) + 10
            else:
                d = d + 4 * x + 6
            
        return coords.append((xc, yc, x, y))




    @classmethod    
    def scale_3D(cls, type='local'):
        pass

    @classmethod
    def draw_object(cls, points_list, canvas):
    # [(x0_0, y0_0, x1_0, y1_0), (x0_1, y0_1, x1_1, y1_1), ...]
    # formato da lista de pontos ^
        for points in points_list:
            x0, y0, x1, y1 = points
            CG.line_breasenham(x0, y0, x1, y1, canvas)


    @classmethod
    def translation_3D(cls):
        pass

    @classmethod
    def rotation_3D(cls):
        pass

    @classmethod
    def shearing_3D(cls):
        pass

    