S1=[k for k in range(0,5)]
A1=[[0,1],[1,4],[0,2],[4,2],[2,3]]
S0=[k for k in range(0,15)]
A0=[[11,14],[11,1],[1,4],[1,14],[2,9],[9,10],[10,5],[2,5],[5,6],[0,3],[3,13],[13,15],[13,7],[7,12],[7,8]]
A3=[[0,1,17],[1,4,23],[0,2,-41],[2,4,37],[2,3,-7]]

A2=[[0,1,8],[4,5,7],[4,-8,4],[7,47,14],[7,23,47]]


def matriceAdjacenceN0(S,A):
    n=len(S)
    tab=[[0 for i in range(n)] for i in range(n)]
    for i in range(n) :
        for j in range(n):
             if i==j:
                 tab[i][j]=0
             elif [i,j] in A or [j,i] in A:
                 tab[i][j]=1
    return tab

print(matriceAdjacenceN0(S1,A1))


def matriceAdjacenceOr(S,A):
    n=len(S)
    tab=[[59 for i in range(n)] for i in range(n)]
    for a in A :
        [i,j,w]=a
        tab[i][j]=w
    return tab
print((matriceAdjacenceOr(S1,A3)))

def maxpoids(A):
    c=A[0][2]
    for i in range (1,len(A)):
        if A[i][2]>c:
            c=A[i][2]
    return c

M0=matriceAdjacenceN0(S1,A1)
def parcour(M,n,i,marque):
    newmarque=marque
    newmarque.add(i)
    for k in range(n):
        if M[i][k]!=0 and k not in newmarque:
            newmarque=parcour(M,n,k,newmarque)
    return newmarque
print(parcour(M0,5,0,set({})))


M1=matriceAdjacenceN0(S0,A0)
def parcourprof(M,n):
    marque=[]
    for k in range(0,n):
        if k not in marque:
            marque=parcour(M,n,k,marque)
#parcourprof(M1,16)

def composante(M,n,i,marque,comp):
    newmarque=marque
    newmarque.add(i)
    newcomposante=comp 
    newcomposante.append(i)
    for k in range(n):
        if M[i][k]!=0 and k not in newmarque:
            composante(M,n,k,newmarque,newcomposante)
    return newmarque,newcomposante
#print(composante(M0,16,0,set({}),[]))

def lescomposantes(M,n):
    marque=set({})
    comp=[]
    for k in range (n):
        if k not in marque:
            marque,comp=composante(M,n,k,marque,[])
            print(comp)


def remonter_chemin(tp,der):
    p=der
    chemin=[p]
    while tp[p]!=p:
        p=tp[p]
        chemin.insert(0,p)
    return chemin

tp=[1,2,2,3,2,4]
for i in range(6):
    print(remonter_chemin(tp,i))

M2=matriceAdjacenceOr(S1,A3)
def matrice_dijsktra(M,s):
    N=len(M[0])
    infini=[0][0]
    A=[]
    C=list(range(N))
    td=[infini for j in range(N)]
    td[s]=0
    tp=[s for i in range(N)]
    while C!=[]:
        C.sort(key=lambda i:td[i])
        a=C[0]
        for c in C:
            if td[a]+M[a][c]<td[c]:
                td[c]=td[a]+M[a][c]
                tp[c]=a
        A.append(a)
        C.remove(a)
    return s,td,tp

print(matrice_dijsktra(M2,0))










                 
