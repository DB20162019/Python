def creer_file():
    f=[]
    return f

def enfiler(v,f):
    f.insert(0,v)

def file_vide(f):
    if len(f)==0:
        return True
    else:
        return False

def desenfiler(f):
    if file_vide(f):
        print("erreur")
    else:
        return f.pop(len(f)-1)
    
def taille(f):
    taille=len(f)
    return(taille)

def premier(f):
    return f[-1]

def afficher_file(f):
    der="dernier entre"
    for i in range (len(f)):
        der=der+str(f[i])+'->'
    print(der)

    
