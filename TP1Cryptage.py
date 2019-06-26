import random as rd

def exp_base(a,n,p):
    x=1
    for i in range(n):
        x=x*a
    y=x % p
    return y

def exp_mod(a,n,p):
    x=a
    y=1
    while n>0:
        if (n%2)!= 0:
            y=y*x % p
            n=n-1
        else:
            x=x*x % p
            n=n/2
    return y

def prim(nb):
    t=0
    racine=int(nb**0.5)
    print(racine)
    for k in range(2,racine+1):
        if (nb%k==0):
            t=1
    if t==0 :
        return True
    else:
        return False

def Fermat(a,p):
    n=Base
    r=exp_mod(n,a-1,a)
    if r==1:
        return True
    else:
        return False

def nb_Euler(n):
    a=[]
    for i in range(1,n+1):
        a=a+[i*i+i+41]
    return a

def nb_pseudo(n):
    a=nb_Euler(n)
    b=[]
    for i in range(n):
        if prim(a[i])==True:
            b=b+[a[i]]
    return b

def pgcd(a,b):
    r=a
    while r!=0:
        r=a%b
        a=b
        b=r
    return a

def clef_publique(p,q):
    if prim(p)==True and prim(q)==True:
        n=p*q
        n2=(p-1)*(q-1)
        e=rd.randint(1,n2)
        while pgcd(n2,e)!=1:
            e=rd.randint(1,n2)
        return(n,e)

def cryptage(x,clef):
    (a,b)=clef
    return exp_mod(x,b,a)

def clef_privee(p,q,e):
    n=((p-1)*(q-1))
    n1=p*q
    d=rd.randint(2,int(n/3))
    while ((e*d-1)%n)!=0:
        d=d+1
    return(n1,d)

def decryptage(y,clef):
    (a,b)=clef
    return exp_mod(y,b,a)




    



#print(prim(12))
#print(exp_base(123456,654321,789))
#print(exp_mod(123456,654321,789))
#print(prim(113))
#print(Fermat(11))
#print(nb_Euler(107))
#print(pgcd(12,24))
#print(clef_publique(7,11))
print(cryptage(3,(77,59)))
#print(clef_privee(7,11,17))
print(decryptage(3,(77,59)))
