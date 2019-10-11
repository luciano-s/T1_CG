from tkinter import *
import numpy as np
import math


class CG:

    def __init__(self):
        self.A = [100, 100, 100, 1]
        self.B = [100, 100, 250, 1]
        self.C = [150, 100, 320, 1]
        self.D = [200, 100, 250, 1]
        self.E = [200, 100, 100, 1]
        self.F = [100, 200, 100, 1]
        self.G = [100, 200, 250, 1]
        self.H = [150, 200, 320, 1]
        self.I = [200, 200, 250, 1]
        self.J = [200, 200, 100, 1]

        self.A2 = [0, 0, 0]
        self.B2 = [0, 0, 0]
        self.C2 = [0, 0, 0]
        self.D2 = [0, 0, 0]
        self.E2 = [0, 0, 0]
        self.F2 = [0, 0, 0]
        self.G2 = [0, 0, 0]
        self.H2 = [0, 0, 0]
        self.I2 = [0, 0, 0]
        self.J2 = [0, 0, 0]

        self.projecao = None
        self.plano = None

        #self.figura = {'A': [self.A, self.A2, 'B', 'E', 'F'], 'B': [self.B, self.B2, 'C', 'D', 'G'],
        #               'C': [self.C, self.C2, 'D', 'H'], 'D': [self.D, self.D2, 'E', 'I'], 'E': [self.E, self.E2, 'J'],
        #               'F': [self.F, self.F2, 'G', 'J'], 'G': [self.G, self.G2, 'H', 'I'], 'H': [self.H, self.H2, 'I'],
        #               'I': [self.I, self.I2, 'J'], 'J': [self.J, self.J2]}

    @classmethod
    def line_breasenham(cls, x0, y0, x1, y1, canvas):
        dx = abs(x1-x0)
        dy = abs(y1-y0)
        d = 0
        if (dy < dx):  # x cresce mais rápido do que y
            if x0 < x1:  # esquerda->direita

                if y0 < y1:  # cima->baixo
                    # octante 1
                    y = y0
                    for x in range(x0, x1+1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if d < 0:
                            d += dy

                        else:
                            d += dy-dx
                            y += 1
                else:  # baixo->cima
                    # octante 8
                    y = y0
                    for x in range(x0, x1+1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if d < 0:
                            d += dy

                        else:
                            d += dy-dx
                            y -= 1
            else:  # direita->esquerda
                if y0 < y1:  # cima->baixo
                    # octante 4
                    y = y0

                    for x in range(x0, x1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if d < 0:
                            d += dy

                        else:
                            d += dy-dx
                            y += 1
                else:  # baixo->cima
                    # octante 5
                    y = y0
                    for x in range(x0, x1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if d < 0:
                            d += dy

                        else:
                            d += dy-dx
                            y -= 1

        else:  # y cresce mais rapido
            if y0 < y1:
                # cima -> baixo
                if x0 < x1:
                    # esquerda->direita
                    # octeto 2
                    x = x0
                    for y in range(y0, y1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if 0 < d:
                            d -= dx
                        else:
                            d += dy-dx
                            x += 1
                else:
                    # direita->esquerda
                    # octeto 3
                    x = x0
                    for y in range(y0, y1+1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if 0 < d:
                            d -= dx
                        else:
                            d += dy-dx
                            x -= 1

            else:
                if x0 < x1:
                    # esquerda->direita
                    # octeto 7
                    x = x0
                    for y in range(y0, y1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if 0 < d:
                            d -= dx
                        else:
                            d += dy-dx
                            x += 1
                else:
                    # direita->esquerda
                    # octeto 6
                    x = x0
                    for y in range(y0, y1, -1):
                        canvas.create_line(x, y, x+1, y+1, fill='#000000')
                        if 0 < d:
                            d -= dx
                        else:
                            d += dy-dx
                            x -= 1

    @classmethod
    def draw_circle(cls, xc, yc, x, y, canvas):
        canvas.create_line(xc+x, yc+y, (xc+x)+1, (yc+y)+1, fill='#000000')
        canvas.create_line(xc-x, yc+y, (xc-x)+1, (yc+y)+1, fill='#000000')
        canvas.create_line(xc+x, yc-y, (xc+x)+1, (yc-y)+1, fill='#000000')
        canvas.create_line(xc-x, yc-y, (xc-x)+1, (yc-y)+1, fill='#000000')
        canvas.create_line(xc+y, yc+x, (xc+y)+1, (yc+x)+1, fill='#000000')
        canvas.create_line(xc-y, yc+x, (xc-y)+1, (yc+x)+1, fill='#000000')
        canvas.create_line(xc+y, yc-x, (xc+y)+1, (yc-x)+1, fill='#000000')
        canvas.create_line(xc-y, yc-x, (xc-y)+1, (yc-x)+1, fill='#000000')

    @classmethod
    def circunferencia(cls, xc, yc, r, canvas):
        print('entrou circunferencia')
        x = 0
        y = r
        d = 3 - 2*r
        CG.draw_circle(xc, yc, x, y, canvas)
        print(f'xc: {xc}, yc: {yc}, x: {x}, y: {y}, r: {r}, d: {d}')
        while y >= x:
            x += 1
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

    @staticmethod
    def projecao(self, canvas):
        if self.projecao == 'cav':
            self.cavaleira(canvas)
        elif self.projecao == 'ort':
            self.ortogonal(canvas, self.plano)
        else:
            self.cabinet(canvas)

    def translacao_3D(self, eixo, deslocamento, canvas):
        if eixo == 'x':
            self.A[0] = self.A[0] + deslocamento
            self.B[0] = self.B[0] + deslocamento
            self.C[0] = self.C[0] + deslocamento
            self.D[0] = self.D[0] + deslocamento
            self.E[0] = self.E[0] + deslocamento
            self.F[0] = self.F[0] + deslocamento
            self.G[0] = self.G[0] + deslocamento
            self.H[0] = self.H[0] + deslocamento
            self.I[0] = self.I[0] + deslocamento
            self.J[0] = self.J[0] + deslocamento
        elif eixo == 'y':
            self.A[1] = self.A[1] + deslocamento
            self.B[1] = self.B[1] + deslocamento
            self.C[1] = self.C[1] + deslocamento
            self.D[1] = self.D[1] + deslocamento
            self.E[1] = self.E[1] + deslocamento
            self.F[1] = self.F[1] + deslocamento
            self.G[1] = self.G[1] + deslocamento
            self.H[1] = self.H[1] + deslocamento
            self.I[1] = self.I[1] + deslocamento
            self.J[1] = self.J[1] + deslocamento
        else:
            self.A[2] = self.A[2] + deslocamento
            self.B[2] = self.B[2] + deslocamento
            self.C[2] = self.C[2] + deslocamento
            self.D[2] = self.D[2] + deslocamento
            self.E[2] = self.E[2] + deslocamento
            self.F[2] = self.F[2] + deslocamento
            self.G[2] = self.G[2] + deslocamento
            self.H[2] = self.H[2] + deslocamento
            self.I[2] = self.I[2] + deslocamento
            self.J[2] = self.J[2] + deslocamento
        
        CG.projecao(self,canvas)

    def cavaleira(self, canvas):
        self.projecao = 'cav'
        Mc = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [((2)**(1/2))/2, ((2)**(1/2))/2, 0, 0],
                       [0, 0, 0, 1]])
        coord1 = 0
        coord2 = 1
        self.A2 = np.dot(np.array(self.A), Mc)
        self.B2 = np.dot(np.array(self.B), Mc)
        self.C2 = np.dot(np.array(self.C), Mc)
        self.D2 = np.dot(np.array(self.D), Mc)
        self.E2 = np.dot(np.array(self.E), Mc)
        self.F2 = np.dot(np.array(self.F), Mc)
        self.G2 = np.dot(np.array(self.G), Mc)
        self.H2 = np.dot(np.array(self.H), Mc)
        self.I2 = np.dot(np.array(self.I), Mc)
        self.J2 = np.dot(np.array(self.J), Mc)

        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.B2[coord1]), int(self.B2[coord2]), fill='black')
        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.E2[coord1]), int(self.E2[coord2]), fill='black')
        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.F2[coord1]), int(self.F2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.C2[coord1]), int(self.C2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.D2[coord1]), int(self.D2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.G2[coord1]), int(self.G2[coord2]), fill='black')
        canvas.create_line(int(self.C2[coord1]), int(self.C2[coord2]), int(
            self.D2[coord1]), int(self.D2[coord2]), fill='black')
        canvas.create_line(int(self.C2[coord1]), int(self.C2[coord2]), int(
            self.H2[coord1]), int(self.H2[coord2]), fill='black')
        canvas.create_line(int(self.D2[coord1]), int(self.D2[coord2]), int(
            self.E2[coord1]), int(self.E2[coord2]), fill='black')
        canvas.create_line(int(self.D2[coord1]), int(self.D2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.E2[coord1]), int(self.E2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')
        canvas.create_line(int(self.F2[coord1]), int(self.F2[coord2]), int(
            self.G2[coord1]), int(self.G2[coord2]), fill='black')
        canvas.create_line(int(self.F2[coord1]), int(self.F2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')
        canvas.create_line(int(self.G2[coord1]), int(self.G2[coord2]), int(
            self.H2[coord1]), int(self.H2[coord2]), fill='black')
        canvas.create_line(int(self.G2[coord1]), int(self.G2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.H2[coord1]), int(self.H2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.I2[coord1]), int(self.I2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')

    def ortogonal(self, canvas, plano):
        self.plano = plano
        self.projecao = 'ort'
        if plano == 'z':
            Mc = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 1]])
            coord1 = 0
            coord2 = 1
            print("z")
        elif plano == 'y':
            Mc = np.array([[1, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
            coord1 = 0
            coord2 = 2
            print("y")
        else:
            Mc = np.array([[0, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
            coord1 = 1
            coord2 = 2
            print("x")

        self.A2 = np.dot(np.array(self.A), Mc)
        self.B2 = np.dot(np.array(self.B), Mc)
        self.C2 = np.dot(np.array(self.C), Mc)
        self.D2 = np.dot(np.array(self.D), Mc)
        self.E2 = np.dot(np.array(self.E), Mc)
        self.F2 = np.dot(np.array(self.F), Mc)
        self.G2 = np.dot(np.array(self.G), Mc)
        self.H2 = np.dot(np.array(self.H), Mc)
        self.I2 = np.dot(np.array(self.I), Mc)
        self.J2 = np.dot(np.array(self.J), Mc)

        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.B2[coord1]), int(self.B2[coord2]), fill='black')
        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.E2[coord1]), int(self.E2[coord2]), fill='black')
        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.F2[coord1]), int(self.F2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.C2[coord1]), int(self.C2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.D2[coord1]), int(self.D2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.G2[coord1]), int(self.G2[coord2]), fill='black')
        canvas.create_line(int(self.C2[coord1]), int(self.C2[coord2]), int(
            self.D2[coord1]), int(self.D2[coord2]), fill='black')
        canvas.create_line(int(self.C2[coord1]), int(self.C2[coord2]), int(
            self.H2[coord1]), int(self.H2[coord2]), fill='black')
        canvas.create_line(int(self.D2[coord1]), int(self.D2[coord2]), int(
            self.E2[coord1]), int(self.E2[coord2]), fill='black')
        canvas.create_line(int(self.D2[coord1]), int(self.D2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.E2[coord1]), int(self.E2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')
        canvas.create_line(int(self.F2[coord1]), int(self.F2[coord2]), int(
            self.G2[coord1]), int(self.G2[coord2]), fill='black')
        canvas.create_line(int(self.F2[coord1]), int(self.F2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')
        canvas.create_line(int(self.G2[coord1]), int(self.G2[coord2]), int(
            self.H2[coord1]), int(self.H2[coord2]), fill='black')
        canvas.create_line(int(self.G2[coord1]), int(self.G2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.H2[coord1]), int(self.H2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.I2[coord1]), int(self.I2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')

    def cabinet(self, canvas):
        self.projecao = 'cab'
        Mc = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [(math.cos(63.4))/2, (math.sin(63.4))/2, 0, 0],
                       [0, 0, 0, 1]])
        coord1 = 0
        coord2 = 1

        self.A2 = np.dot(np.array(self.A), Mc)
        self.B2 = np.dot(np.array(self.B), Mc)
        self.C2 = np.dot(np.array(self.C), Mc)
        self.D2 = np.dot(np.array(self.D), Mc)
        self.E2 = np.dot(np.array(self.E), Mc)
        self.F2 = np.dot(np.array(self.F), Mc)
        self.G2 = np.dot(np.array(self.G), Mc)
        self.H2 = np.dot(np.array(self.H), Mc)
        self.I2 = np.dot(np.array(self.I), Mc)
        self.J2 = np.dot(np.array(self.J), Mc)

        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.B2[coord1]), int(self.B2[coord2]), fill='black')
        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.E2[coord1]), int(self.E2[coord2]), fill='black')
        canvas.create_line(int(self.A2[coord1]), int(self.A2[coord2]), int(
            self.F2[coord1]), int(self.F2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.C2[coord1]), int(self.C2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.D2[coord1]), int(self.D2[coord2]), fill='black')
        canvas.create_line(int(self.B2[coord1]), int(self.B2[coord2]), int(
            self.G2[coord1]), int(self.G2[coord2]), fill='black')
        canvas.create_line(int(self.C2[coord1]), int(self.C2[coord2]), int(
            self.D2[coord1]), int(self.D2[coord2]), fill='black')
        canvas.create_line(int(self.C2[coord1]), int(self.C2[coord2]), int(
            self.H2[coord1]), int(self.H2[coord2]), fill='black')
        canvas.create_line(int(self.D2[coord1]), int(self.D2[coord2]), int(
            self.E2[coord1]), int(self.E2[coord2]), fill='black')
        canvas.create_line(int(self.D2[coord1]), int(self.D2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.E2[coord1]), int(self.E2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')
        canvas.create_line(int(self.F2[coord1]), int(self.F2[coord2]), int(
            self.G2[coord1]), int(self.G2[coord2]), fill='black')
        canvas.create_line(int(self.F2[coord1]), int(self.F2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')
        canvas.create_line(int(self.G2[coord1]), int(self.G2[coord2]), int(
            self.H2[coord1]), int(self.H2[coord2]), fill='black')
        canvas.create_line(int(self.G2[coord1]), int(self.G2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.H2[coord1]), int(self.H2[coord2]), int(
            self.I2[coord1]), int(self.I2[coord2]), fill='black')
        canvas.create_line(int(self.I2[coord1]), int(self.I2[coord2]), int(
            self.J2[coord1]), int(self.J2[coord2]), fill='black')

    @classmethod
    def rotation_3D(cls):
        pass

    @classmethod
    def shearing_3D(cls):
        pass



def main():
    root = Tk()
    root.title('Casinha')
    canvas = Canvas(root, width=2000, height=2000, background='#ffffff')
    canvas.grid(row=0, column=0)
    a = CG()
    #a.cavaleira(canvas)
    #a.translacao_3D('x', 300, canvas)
    #a.cabinet(canvas)
    #a.translacao_3D('y', 300, canvas)
    #a.ortogonal(canvas, 'y')
    #a.translacao_3D('x', 200, canvas)
    root.mainloop()


main()
