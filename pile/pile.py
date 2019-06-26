def creer_pile():
    p=[]
    return(p)


def est_vide(p):
    if len(p)==0:
        return(True)
    else:
        return(False)


def depiler(p):
    if est_vide(p):
        print("erreur")
    else:
        return p.pop()


def empiler(v,p):
    p.append(v)
    

def taille(p):
    taille=len(p)
    return(taille)


def sommet(p):
    return Tab[len(p)-1]


def afficher_pile(p):
    print('sommet')
    i=len(p)
    while i>0:
      i-=1
      print('| '+str(p[i])+' |')

