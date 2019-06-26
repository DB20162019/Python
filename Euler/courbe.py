import numpy as np
import matplotlib.pyplot as plt

def derivee_UC(Uc_t,t,U0,C,R):
    dUc=0
    dUc=(U0-Uc_t)/(RC)
    return dUc

def euler(dUC,y0,pas,nb_iterations):
    tab=[0 for i in range(nb_iterations)]
    tab[0]=y0
    p=pas
    for k in range (1,nb_iterations):
        tab[k]=tab[k-1]+p*dUC
    return tab

def influence_pas():
    t=[5,10,50,100,500,1000]
    for i in range(len(t)):
        p[i]=0,01/t[i]
        euler(dUc,y0,p[i],t[i])
    return euler

def Euler2(a,b,phi,y0,n):
    tab=[0 for i in range(n)]
    t=[0 for i in range(n)]
    tab[0]=y0
    c=0
    d=(b-a)/n
    for k in range (1,n):
        t[k]=a+k*d
        tab[k]=tab[k-1]+phi(c,tab[k-1])*d
    return np.array(t),np.array(tab)

abs=t
ord=tab
plt.plot(abs,ord,'o')
plt.show()

    


                                


    
