
def lettre_numero(message):
    l=[]
    x=0
    for i in range(len(message)):
        x=int(ord(message[i])-64)
        l.append(x)
    return l




def liste_liste_code(liste_de_nombres):
    l=[]
    n=0
    y=0
    for i in range(len(liste_de_nombres)):
        n=3*(liste_de_nombres[i])
        y=(n+5)%26
        l.append(y)
    return l



def numero_lettre(liste_de_nombres):
    x=''
    for i in range(len(liste_de_nombres)):
        x+=chr(liste_de_nombres[i]+64)
    return x

def codage(message):
    a=lettre_numero(message)
    b=liste_liste_code(a)
    c=numero_lettre(b)
    return c
print(codage('JOUR'))

def liste_liste_decode(liste_de_nombres):
    l=[]
    a=0
    b=0
    for i in range(len(liste_de_nombres)):
        a=9*(liste_de_nombres[i])
        b=(a+7)%26
        l.append(b)
    return l


def decodage(message):
    a=lettre_numero(message)
    b=liste_liste_decode(a)
    c=numero_lettre(b)
    return c

print(decodage('IXPG'))

def fichier(nomfichier):
    ob=open(nomfichier,'r')
    l=ob.read()
    a=codage(l)
    ob.close()
    obj=open(nom,'w')
    obj.write(a)
    obj.close()
    
    
