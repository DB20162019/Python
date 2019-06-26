def conversion (n):
    tab=[]
    while n!=0:
        r=n%2
        n=n//2
        tab.append(r)
    return tab


def puissance(n):
    tab=[]
    i=0
    while n-2**i>0:
        i=i+2
    i=i-1
    tab.append(1)
    n=n-2**i
    for j in range(i):
        if n-2**(i-j)>0:
            tab.append(1)
        else:
            tab.append(0)
    return tab


print(conversion(124))
print(puissance(97))
    
def division_successive(n):
    tab=[]
#je n'ai pas compris en quoi cette fonction est différente de la première qui utilise aussi les divisions successives

    

def conversion_bits(n):
    tab=[]
    a=0
    if n<0:
        a=n+256
        conversion(a)
    else:
        a=n
        conversion(n)


print(conversion_bits(87))
#ça ne fonctionne pas c'est un problème avec la fonction conversion


def bits_entier(n):
    tab=[]
    somme=0
    for i in range (len(n)):
        somme=somme+2**tab[i]
        tab.append(i)
    return somme

