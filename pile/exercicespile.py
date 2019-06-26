import pile as pile

def deux_elements(a,b):
    p=creer_pile()
    if len(p)>=2:
        a=depiler(p)
        b=depiler(p)
        a=empiler(p)
        b=empiler(p)
    print(afficher_pile(p))
    

