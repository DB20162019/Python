import pile as pile
from copy import deepcopy

def interversion(p):
    if pile.taille(p)>=2:
        a=pile.depiler(p)
        b=pile.depiler(p)
        pile.empiler(a,p)
        pile.empiler(b,p)




def troisieme_element(p):
    if pile.taille(p)>=3:
        a=pile.depiler(p)
        b=pile.depiler(p)
        c=pile.depiler(p)
        pile.empiler(b,p)
        pile.empiler(a,p)
        return c


def copier_pile(p):
    pil=pile.creer_pile()
    copie=deepcopy(p)
    while pile.taille(copie)>0:
        a=pile.depiler(copie)
        pile.empiler(a,pil)
    while pile.taille(pil)>0:
        b=pile.depiler(pil)
        pile.empiler(b,pil)
    pile.afficher_pile(p)
    pile.afficher_pile(pil)
    

def inverser_pile(p):
    pil=pile.creer_pile()
    a=pile.creer_pile()
    a=deepcopy(p)
    while pile.taille(a)>0:
        b=pile.depiler(a)
        pile.empiler(b,pil)
    pile.afficher_pile(p)
    pile.afficher_pile(pil)



def d2b(n):
    tab=[]
    while n>=1:
        r=n%2
        n=n//2
        tab.append(r)
    while 0<n<1:
        r=n%2
        n=n//2**-1
        tab.append(r)
    return tab


def b2d(s):
    p=pile.creer_pile()
    s=0
    for i in range (pile.taille(p)): 
            pile.inverser_pile(p)
            s=p[i]*2**i
        return s

    
###5)2) oui, on a besoin d'une pile car les 0 et 1 sont mis dans un tableau et ensuite pour inverser le sens du tableau
    
