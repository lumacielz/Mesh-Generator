#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:28:35 2021

@author: luiza.maciel
"""


import numpy as np
import matplotlib.pyplot as plt

print("------------------------------GERADOR DE MALHAS----------------------------------")

while True:
    try:
        Lx=float(input("comprimento em x: "))
        Ly=float(input("comprimento em y: "))
        
        nx=int(input("numero de nós em x: "))
        ny=int(input("numero de nós em y: "))
        break
    except:
        print("Valor inválido!")

size=input("[0] elementos igualmente espaçados [1] elementos com tamanho variavel")

while True:
    if size == "1":
        dx=map(lambda x: float(x), list(input("tamanho de cada elemento em x: ")))
        dy=map(lambda y: float(y), list(input("tamanho de cada elemento em y: ")))
        break
    elif size == "0":
        dx=[Lx/(nx-1) for n in range(nx)]
        dy=[Ly/(ny-1) for n in range(ny)]
        break
    else:
        print("Opção inválida!")
        continue

if Ly != 0 and Lx != 0: 
    ne = (nx-1)*(ny-1)
    shape=input("forma dos elementos [TRI]  [QUAD]: ") 

npoints = nx*ny

X = np.zeros( (npoints),dtype='float' )
Y = np.zeros( (npoints),dtype='float' )

IEN=[]

#generate X
for j in range (0,ny):
    for i in range(1,nx):
        X[i+(j)*nx] = X[i-1]+dx[i-1]
  
#generate Y
for j in range (1,ny):
    for i in range(0,nx):
        Y[i+j*nx]=Y[(j-1)*nx]+dy[j-1]
        

print(X,Y)

#IEN
def genIENQuad(nx,ny):
    up=0
    for j in range (0,ny-1):
        for i in range(0,nx-1):
            quad=[up+i,up+i+1,up+nx+i+1,up+nx+i]
            IEN.append(quad)
        up+=nx
    plt.plot(X,Y,'o')
    return IEN

def genIENTri(nx,ny):
    up=0
    for j in range (0,ny-1):
        for i in range(0,nx-1):
            tri1=[up+i,up+nx+i+1,up+nx+i]
            tri2=[up+i,up+i+1,up+nx+i+1]
            IEN.append(tri1)
            IEN.append(tri2)
        up+=nx
    plt.triplot(X,Y,IEN,'ko-')
    return IEN

def gen1D(L,n,v):
    X = np.linspace(0,L,n)
    IEN = np.zeros((n,2),dtype='int')
    for i in range(0,ne):
        IEN[i] = [i,i+1]
    if v:
        plt.plot(np.zeros(n),X,'o')
    else:
        plt.plot(X,np.zeros(n),'o')

def genContour(nx,ny):
    contour,middle=[],[]
    for e in range(0,npoints):
        for j in range(0,ny):
            if e == j*nx or e == j*nx+nx-1 or e in (list(range(1,nx-1))+list((range(1+(ny-1)*nx,nx*ny-1)))):
                contour.append(e)
                break
        if e not in contour:
            middle.append(e)
    print("Nós de contorno: " + str(contour), "/n Nós que não pertencem ao contorno: "+ str(middle))
    
    
if Ly == 0:
    gen1D(Lx,nx,False)
elif Lx == 0:
    gen1D(Ly,ny,True)
    
    
elif shape == "QUAD":
    genIENQuad(nx,ny)
elif shape == "TRI":
    genIENTri(nx,ny)
genContour(nx,ny)

plt.show()

        
