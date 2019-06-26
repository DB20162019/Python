import PIL.Image as image
import numpy as np
import math




def save_img(m,nom): 
    n=len(m)
    p=len(m[0])
    m = np.reshape(m,n*p)
    dam_mb = image.new('L',(n,p))
    dam_mb.putdata(m)
    #dam_mb.show()
    dam_mb.save(nom)

    


def normalise(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j]=int(min(255,max(0,m[i][j])))
    return m



def convolution(m,noyau):
    n=len(m)
    p=len(m[0])
    M=[[0 for j in range(p)]for i in range(n)]
    for i in range(1,n-1):
        for j in range(1,p-1):
            M[i][j]=noyau[0][0]*m[i-1][j-1]+noyau[0][1]*m[i-1][j]+noyau[0][2]*m[i-1][j+1]+noyau[1][0]*m[i][j-1]+noyau[2][0]*m[i+1][j-1]+noyau[2][1]*m[i+1][j]+noyau[2][2]*m[i+1][j+1]+noyau[1][2]*m[i][j+1]+noyau[1][1]*m[i][j]
    return normalise(M)

noyau1=[[1./9,1./9,1./9],[1./9,1./9,1./9],[1./9,1./9,1./9]]
mb=image.open('lena_gris.bmp')
mbtab=np.array(mb)
a=convolution(mbtab,noyau1)
save_img(a,'lena4.bmp')


def moravec(m,dx,dy):
    n=len(m)
    p=len(m[0])
    M=[[0 for j in range(p)]for i in range(n)]
    for i in range(-n+1,n-1):
        for j in range(-n+1,n-1):
            
        
