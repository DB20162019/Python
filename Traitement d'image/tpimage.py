import numpy as np
import PIL.image as im
import math


def negatif(image):
    mbtab=mb.array(image)
    n,p=mbtab.size
    for i in range(n):
        for j in range(p):
            mbtab[i][j]=255-mbtab[i][j]
    return mbtab

def traitement_p(mbtab,f):
    n,p=mbtab.size
    for i in range(n):
        for j in range(p):
            mbtab[i][j]= f(mbtab[i][j])
    return mbtab

def negatif2(x):
    return 255-x

def racinecarre(x):
    f=int((255**(1/2))*(x**(1/2)))
    return f

##La fonction eclaircie l'image : on obtient une image plus claire

def assombri(x):
    f=int((255**2)*(x**2))
    return f

def gamma(x,y):
    f=lambda x y : x**y
    return f 

def foncg(x):
    g=lamda x: 0.5+0.5*math.sin(x-0.5)*math.pi
    return g



def convo
    
    
    
    
    






    
    
    
    
    
