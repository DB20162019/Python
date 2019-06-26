import pile as pile
from copy import deepcopy

def intervertion(p):
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



def inverser_pile(p):
    pil=pile.creer_pile()
    a=pile.creer_pile()
    a=deepcopy(p)
    while pile.taille(a)>0:
        b=pile.depiler(a)
        pile.empiler(b,pil)


    
def copier_pile(p):
    pil=pile.creer_pile()
    pil=inverser_pile(p)
    pil=inverser_pile(pil)
    pile.afficher(p)
    pile.afficher(pil)
    




p=[0,4,5,8,7]
print(copier_pile(p))
    

    
