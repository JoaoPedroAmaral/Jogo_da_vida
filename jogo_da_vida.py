#jogo da vida
import turtle as t
from random import random

#config
altura=50
largura=50

def mat_zero(a, l, f):
    nova=[]
    for i in range(a):
        nova.append([False]*l)
    if f>0:
        for i in range (a):
            for j in range (l):
                nova[i][j] = random() < f
    return nova
        
#desenhar matriz
def mat_desenhar(t, mat):
    t.tracer(0)
    t.reset()
    t.pu()
    t.ht()
    t.width(5)
    hor_dist= largura //2 *10
    ver_dist = altura //2 *10
    for a in range (altura):
        for l in range (largura):
            t.goto(l*10 - hor_dist, a*10 - ver_dist)
            if mat[a][l]: t.dot()
            
    t.update()
    
def simula (mat):
    nova = mat_zero (altura, largura, 0)
    for a in range (altura):
        for l in range (largura):
            am= (a+1) % altura
            lm= (l+1) % largura
            soma= (mat[a-1][l] + mat[am][l] +
                   mat[a][l-1] + mat[a][lm] +
                   mat[a-1][l-1] + mat[am][lm] +
                   mat[a-1][lm] + mat[am][l-1])
            if mat[a][l]:
                if soma < 2: nova[a][l] = False
                elif soma > 3: nova[a][l] = False
                else: nova[a][l] = True
            else:
                if soma == 3: nova[a][l] = True
    return nova 
      
def atualizar():
    global mat
    mat=simula(mat)
    mat_desenhar(t, mat)
    t.ontimer(atualizar, 10)
        
#teste
mat=mat_zero(altura, largura, 0.3)
atualizar()
t.mainloop()
