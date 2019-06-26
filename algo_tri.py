import random
a=[random.randint(1,100) for i in range(10)]
print(a)

def tri(a):
    for i in range(1,len(a)):
        j=0
        while j!=i:
            if a[i]<=a[j]:
                c=a[i]
                a[i]=a[j]
                a[j]=c
            j=j+1

tri(a)
print(a)

def echange(a,i,j):
    a[i],a[j]=a[j],a[i]

def partition(a,g,d):
    p=random.randint(g,d-1)
    print(a[p])
    v=a[p]
    echange(a,g,p)
    m=g
    for i in range(g+1,d):
        if a[i]<v:
            m=m+1
            echange(a,i,m)
    if m!=g:
        echange(a,g,m)
    return (m+1)
print(partition(a,0,len(a)))
print(a)


def fusion(a1,a2,g,m,d):
    i,j=g,m
    for k in range (g,d):
        if i<m and (j==d or a1[i]<=a1[j]):
            a2[k]=a1[i]
            i+=1
        else:
            a2[k]=a[j]
            j+=1
print(fusion(a1,[],0,len(a1)/2,len(a1)))
