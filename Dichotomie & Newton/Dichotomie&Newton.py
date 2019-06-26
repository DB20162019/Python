import random as rd

def dich_solve(f,n,a,b):
    while b-a>(10**-n):
        m=(a+b)/2.0
        if f(a)*f(m)<0:
            a,b=a,m
        else:
            a,b=m,b
    return (a+b)/2.0


f=lambda x:(x**3)-3*(x**2)+1


def recherche(l,e):
    for i in range(len(l)-1):
        if l[i]==e:
            return True
        else:
            return False

def dich_search2(l,e):
    Imin=0
    Imax=len(l)-1
    while Imax-Imin>=0:
        Imed=(Imin+Imax)//2
        if l[Imed]==e:
            return True
        elif l[Imed]<e:
            Imin=Imed+1
        else:
            Imax=Imed-1
    return False
    
    
    
e=2
l=[0,2,4,7,9]
print(dich_search2(l,e))

def racine_trinome(a,b,c):
    delta=(b**2)-(4*a*c)
    x1=0
    x2=0
    if delta==0:
        x1=-b/(2*a)
        return x1
    elif delta>0:
        x1=(-b-(delta)**(1/2))/(2*a)
        x2=(-b+(delta)**(1/2))/(2*a)
        return x1,x2
    else:
        return False



print(racine_trinome(1,1,(1.0-2**-54)/4.0))

def newton(f,df,x,n):
    
    
    
    




