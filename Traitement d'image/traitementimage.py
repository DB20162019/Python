import PIL.Image as image
import numpy as np

#mb=image.open('lena.tiff')
#mb.size
#mb_gris= mb.convert('L')
#mb_gris.save('lena_gris.bmp')

#mbtab=np.array(mb)
#for lignes in mbtab:
#    for m in lignes:
#        m[0],m[1]=m[1],m[0]

#mb_new=image.fromarray(mbtab)
#mb_new.save('lena.bmp')
#le traitement transforme l'image en image verte



def nombrepixel(mb):
    mb_g=image.open(mb)
    mbtab=np.array(mb_g)
    a=len(mbtab)
    b=len(mbtab[0])
    c=0
    d=0
    for i in range(a):
        for j in range(b):
            if mbtab[i][j]==0:
                c=c+1
            elif mbtab[i][j]==255:
                d=d+1
    return c,d


def save_img(m,nom): 
    n=len(m)
    p=len(m[0])
    m = np.reshape(m,n*p)
    dam_mb = image.new('L',(n,p))
    dam_mb.putdata(m)
    #dam_mb.show()
    dam_mb.save(nom)


    
def aggrandgris(im):
    mb=image.open(im)
    mbtab=np.array(mb)
    a=len(mbtab)
    b=len(mbtab[0])
    mbt=[[0 for j in range(b*2)]for i in range(a*2)]
    for i in range(a):
        for j in range(b):
            jA=0
            iA=0
            jA=j+1
            iA=i+1
            mbt[i][j]= mbtab[i][j]
            mbt[i][jA]=mbtab[i][j]
            mbt[iA][j]=mbtab[i][j]
            mbt[iA][jA]=mbtab[i][j]
    save_img(mbt,'lenaaggr.bmp')


def aggrand(im):
    mb=image.open(im)
    mbtab=np.array(mb)
    a=len(mbtab)
    b=len(mbtab[0])
    mbt=[[0 for j in range(b*2)]for i in range(a*2)]
    for i in range(a):
        for j in range(b):
            jA=0
            iA=0
            jA=j+1
            iA=i+1
            mbt[i][j]= mbtab[i][j]
            mbt[i][jA]=mbtab[i][j]
            mbt[iA][j]=mbtab[i][j]
            mbt[iA][jA]=mbtab[i][j]
    mbi=image.fromarray(mbt)
    mbi.save('lena2.bmp')



def imsymetrique(im):
    mb=image.open(im)
    mbtab=np.array(mb)
    a=len(mbtab)
    b=len(mbtab[0])
    tab=[[0 for j in range(b)]for i in range(a)]
    for i in range(a-1):
        for j in range(b-1):
            tab[i][j]=mbtab[i][-j]
    save_img(tab,'lenasym.bmp')

def rotation(im):
    mb=image.open(im)
    mbtab=np.array(mb)
    a=len(mbtab)
    b=len(mbtab[0])
    tab=[[0 for j in range(b)]for i in range(a)]
    for i in range(a-1):
        for j in range(b-1):
            tab[i][j]= mbtab[j][i]
    save_img(tab,'lenarot.bmp')

    
def damier(n,p):
    tab=np.zeros((n,p),dtype=np.uint8)
    for i in range(n):
        for j in range(p):
            if(i+j)%2==0:
                tab[i][j]=0
            else :
                tab[i][j]=255
    t=image.fromarray(tab)
    t.save('damier.bmp')




noyau1=[[1./9,1./9,1./9],[1./9,1./9,1./9],[1./9,1./9,1./9]]
noyau2=[-1,0,1]
noyau3=[1,0,-1]
SobelX_G1=[[-1,-2,-1],[0,0,0],[1,2,1]]
SobelX_G2=[[1,2,1],[0,0,0],[-1,-2,-1]]
SobelY_G1=[[-1,0,1],[-2,0,2],[-1,0,1]]
SobelY_G2=[[1,0,-1],[2,0,-2],[1,0,-1]]
Robert_G1=[[0,0,1],[0,0,0],[-1,0,0]]
Robert_G2=[[0,0,-1],[0,0,0],[1,0,0]]
Prewitt_G1=[[-1,0,1],[-1,0,1],[-1,0,1]]
Prewitt_G2=[[1,1,1],[0,0,0],[-1,-1,-1]]
MavoVassy_G1=[[0,1,1],[-1,0,1],[-1,-1,0]]
MavoVassy_G2=[[1,1,0],[1,0,-1],[0,-1,-1]]
