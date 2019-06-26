import file as file


def permutation_circulaire(q,i):
    for j in range (i):
        a=file.desenfiler(q)
        file.enfiler(a,q)



def Hamming(n):
    f1=file.creer_file()
    file.enfiler(1,f1)    
    f3=file.creer_file()
    file.enfiler(1,f3)  
    f5=file.creer_file()
    file.enfiler(1,f5)
    a=file.premier(f1)
    b=file.premier(f3)
    c=file.premier(f5)
    while n>0:
        if (a<b) and (a<c):
            k=a
            print(k)
        elif (b<a) and (b<c):
            k=b
            print(k)
        elif (c<a) and (c<b):
            k=c
            print(k)
        f=2*k
        g=3*k
        h=5*k
        if k==f1:
            file.desenfiler(f1)
        elif k==f3:
            file.desenfiler(f3)
        elif k==f5:
            file.desenfiler(f5)
        while k<n:
            file.enfiler(f,f1)
            file.enfiler(g,f3)
            file.enfiler(h,f5)


Hamming(10)

