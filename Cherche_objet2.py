from random import randrange as rand
from turtle import *
import time

def labyrinthe():
    ht()
    largeur = rand(5,25)
    hauteur = rand(5,25)
    largeur = 20
    hauteur = 20
    print("largeur: ",largeur," hauteur: ",hauteur,"\n")
    grille = []
    for j in range(hauteur):
        grille.append([])
        for i in range(largeur):
            grille[j].append([1,1,1,1])
    tab_val = []
    for j in range(hauteur):
        tab_val.append([0]*largeur)
    for j in range(hauteur):
        for i in range(largeur):
            tab_val[j][i] = (j*largeur)+i
    cases_avec_voisins = set([(0,0)])
    voisins = vois(0,0,largeur,hauteur,tab_val)
    cases_non_visitees = set(list(voisins))
    while len(cases_non_visitees) != 0:
        choix_case = False
        while not choix_case:
            case = list(cases_avec_voisins)[rand(0,len(cases_avec_voisins))]
            voisins = vois(case[0],case[1],largeur,hauteur,tab_val)
            if len(voisins) != 0:
                choix_case = True
            else:
                cases_avec_voisins.remove(case)
        voisin = list(voisins)[rand(0,len(voisins))]
        diff_abs = voisin[0]-case[0]
        diff_ord = voisin[1]-case[1]
        if diff_abs == 1:
            grille[case[1]][case[0]][0] = 0
            grille[voisin[1]][voisin[0]][2] = 0
        elif diff_abs == -1:
            grille[case[1]][case[0]][2] = 0
            grille[voisin[1]][voisin[0]][0] = 0
        elif diff_ord == 1:
            grille[case[1]][case[0]][3] = 0
            grille[voisin[1]][voisin[0]][1] = 0
        else:
            grille[case[1]][case[0]][1] = 0
            grille[voisin[1]][voisin[0]][3] = 0
        tab_val[voisin[1]][voisin[0]] = 0
        cases_non_visitees.remove(voisin)
        voisins.remove(voisin)
        if len(voisins) == 0:
            cases_avec_voisins.remove(case)
        voisins = vois(voisin[0],voisin[1],largeur,hauteur,tab_val)
        if len(voisins) != 0:
            cases_avec_voisins.add(voisin)
        for v in voisins:
            cases_non_visitees.add(v)
    color("black")
    speed("fastest")
    width(1)
    up()
    goto(-775,400)
    down()
    forward(20*largeur)
    up()
    goto(-775+20*largeur,400-20)
    down()
    sens = -1
    for j in range(hauteur-1):
        if sens == 1:
            for i in range(largeur):
                if grille[j][i][3] == 1:
                    forward(20)
                else:
                    up()
                    forward(20)
                    down()
            sens = -1
            tp = pos()
            up()
            goto(tp[0],tp[1]-20)
            down()
        else:
            k = largeur-1
            while k > -1:
                if grille[j][k][3] == 1:
                    backward(20)
                else:
                    up()
                    backward(20)
                    down()
                k -= 1
            sens = 1
            tp = pos()
            up()
            goto(tp[0],tp[1]-20)
            down()
    if sens == 1:
        forward(20*largeur)
    else:
        backward(20*largeur)
    left(90)
    forward(20*hauteur)
    if sens == -1:
        up()
        tp = pos()
        goto(tp[0]+20,tp[1])
        down()
        for i in range(1,largeur):
            if sens == -1:
                for j in range(hauteur):
                    if grille[j][i][2] == 1:
                        backward(20)
                    else:
                        up()
                        backward(20)
                        down()
                sens = 1
                up()
                tp = pos()
                goto(tp[0]+20,tp[1])
                down()
            else:
                k = hauteur-1
                while k > -1:
                    if grille[k][i][2] == 1:
                        forward(20)
                    else:
                        up()
                        forward(20)
                        down()
                    k -= 1
                sens = -1
                up()
                tp = pos()
                goto(tp[0]+20,tp[1])
                down()
        if sens == -1:
            backward(20*hauteur)
        else:
            forward(20*hauteur)
                                
    else:
        up()
        tp = pos()
        goto(tp[0]-20,tp[1])
        down()
        i = largeur-2
        while i > -1:
            if sens == 1:
                for j in range(hauteur):
                    if grille[j][i][0] == 1:
                         backward(20)
                    else:
                         up()
                         backward(20)
                         down()
                sens = -1
                up()
                tp = pos()
                goto(tp[0]-20,tp[1])
                down()
            else:
                k = hauteur -1
                while k > -1:
                    if grille[k][i][0] == 1:
                        forward(20)
                    else:
                        up()
                        forward(20)
                        down()
                    k -= 1
                sens = 1
                up()
                tp = pos()
                goto(tp[0]-20,tp[1])
                down()
            i-=1
        if sens == 1:
            backward(20*hauteur)
        else:
            forward(20*hauteur)
    up()
    goto(-775+10,400-10)
    right(90)
    down()
    return (largeur,hauteur,grille)

def vois(abs,ord,largeur,hauteur,tab_val):
    voisins = set()
    if abs > 0 and tab_val[ord][abs-1] != 0:
        voisins.add((abs-1,ord))
    if abs < largeur-1 and tab_val[ord][abs+1] != 0:
        voisins.add((abs+1,ord))
    if ord > 0 and tab_val[ord-1][abs] != 0:
        voisins.add((abs,ord-1))
    if ord < hauteur-1 and tab_val[ord+1][abs] != 0:
        voisins.add((abs,ord+1))
    return voisins

def cherche(abs_objet,ord_objet,abs_reelle,ord_reelle,grille,hauteur,largeur):
    ht()
    speed("fastest")
    width(3)
    color("red")
    up()
    tp = pos()
    goto(tp[0]+20*abs_objet,tp[1]-20*ord_objet-5)
    down()
    circle(5)
    time.sleep(2)
    up()
    goto(-775+10,400-10)
    tp = pos()
    goto(tp[0]+20*abs_reelle,tp[1]-20*ord_reelle)
    down()
    print(abs_reelle,ord_reelle,abs_objet,ord_objet)
    print("aller")
    #print("abs: ",0," ord:",0)
    speed(6)
    #Initialisation des coordonnees de la memoire
    (min_abs,max_abs,min_ord,max_ord,abs,ord) = (0,0,0,0,0,0)
    #Initialisation de la memoire
    mem      = [[-2]]
    mem_laby = [[-1]]
    #Creation de dictionnaires
    val_dir = {1:(1,0),2:(0,-1),3:(-1,0),4:(0,1)}
    dir     = {1:(4,1,2,3),2:(1,2,3,4),3:(2,3,4,1),4:(3,4,1,2)}
    #Direction de depart
    direct   = 2
    compteur = 0
    width(3)
    color("red")
    begin_fill()
    right(45)
    forward(7)
    backward(14)
    forward(7)
    right(90)
    forward(7)
    backward(14)
    forward(7)
    left(135)
    end_fill()
    time.sleep(0.5)
    st()
    #Boucle sur les coordonnees
    while abs_reelle != abs_objet or ord_reelle != ord_objet:
        min = mem[ord-min_ord][abs-min_abs]
        i   = 0
        direction = dir[direct]
        avance = False
        #Recherche des murs
        murs = grille[ord_reelle][abs_reelle]
        while not avance:
            #Cas d'une impasse
            if murs[direction[0]-1] == 1 and murs[direction[1]-1] == 1 and murs[direction[2]-1] == 1 and mem[ord-min_ord][abs-min_abs] != -1:
                direct = direction[3]
                mem[ord-min_ord][abs-min_abs] = compteur
                compteur += 1
                avance = True
            else :
                #Variables temporaires
                (temp_min_abs,temp_max_abs,temp_min_ord,temp_max_ord) = (abs,abs,ord,ord)
                val = direction[i]
                if murs[val-1] == 1: i += 1
                else:
                    if val == 1: temp_max_abs += 1
                    if val == 2: temp_min_ord -= 1
                    if val == 3: temp_min_abs -= 1
                    if val == 4: temp_max_ord += 1
                    #Cas d'une case non inscrite dans la memoire
                    if temp_max_abs > max_abs or temp_max_ord > max_ord or temp_min_abs < min_abs or temp_min_ord < min_ord:
                        #Creation de la case
                        construction_mem(mem,abs,ord,val,max_abs,max_ord,min_abs,min_ord,mem_laby)
                        direct = val
                        avance = True
                    else:
                        choix = mem[ord + val_dir[val][1]-min_ord][abs + val_dir[val][0]-min_abs]
                        #Cas d'une case non visitee
                        if choix == -2:
                            direct = val
                            avance = True
                        #Cas d'une case deja visitee
                        if choix < min:
                            l   = val
                            min = choix
                        i += 1
                if i == 4:
                    avance = True
                    direct = l
        #Variables temporaire
        (temp_abs,temp_ord) = (abs,ord)
        #Deplacement
        color("green")
        speed("fastest")
        width(3)
        if direct == 1:
            abs_reelle += 1
            abs        += 1
            forward(20)
            if abs > max_abs : max_abs = abs
        if direct == 2:
            ord_reelle -= 1
            ord        -= 1
            tp = pos()
            goto(tp[0],tp[1]+20)
            if ord < min_ord: min_ord = ord
        if direct == 3:
            abs_reelle -= 1
            abs        -= 1
            backward(20)
            if abs < min_abs : min_abs = abs
        if direct == 4:
            ord_reelle += 1
            ord        += 1
            tp = pos()
            goto(tp[0],tp[1]-20)
            if ord > max_ord: max_ord = ord
        #Changement de valeur des cases
        mem_laby[temp_ord-min_ord][temp_abs-min_abs] = murs
        dessin = 1
        if mem[temp_ord-min_ord][temp_abs-min_abs] == -2:
            mem[temp_ord-min_ord][temp_abs-min_abs] = compteur
            compteur += 1
        #print("abs: ",abs,",ord: ",ord)
   
    mem_laby[ord-min_ord][abs-min_abs] = grille[ord_reelle][abs_reelle]
    return (mem,mem_laby,abs,ord,min_abs,min_ord,max_abs,max_ord,compteur)

    
def construction_mem(mem,abs,ord,direct,max_abs,max_ord,min_abs,min_ord,mem_laby):
    if direct == 1:
        temp_abs = abs+1
        for j in range(len(mem)):
            mem[j].append(-2)
            mem_laby[j].append(-1)
    if direct == 4:
        temp_ord = ord+1
        mem.append([-2]*len(mem[0]))
        mem_laby.append([-1]*len(mem_laby[0]))
    if direct == 2:
        temp_ord = ord-1
        mem.insert(0,[-2]*len(mem[0]))
        mem_laby.insert(0,[-1]*len(mem_laby[0]))
    if direct == 3:
        temp_abs = abs-1
        for i in range(len(mem)):
            mem[i].insert(0,-2)
            mem_laby[i].insert(0,-1)


#fonction retourne
def retour(mem,mem_laby,abs,ord,min_abs,min_ord,max_abs,max_ord,compteur):
    print("retour")
    width(3)
    speed(6)
    while abs != 0 or ord != 0:
        abs_mem = abs-min_abs
        ord_mem = ord-min_ord
        murs = mem_laby[ord_mem][abs_mem]
        cases_voisines = []
        if abs +1 <= max_abs : cases_voisines.append([(abs+1,ord),mem[ord_mem][abs_mem+1]])
        else : cases_voisines.append([-2,-2])
        if ord -1 >= min_ord : cases_voisines.append([(abs,ord-1),mem[ord_mem-1][abs_mem]])
        else : cases_voisines.append([-2,-2])
        if abs -1 >= min_abs : cases_voisines.append([(abs-1,ord),mem[ord_mem][abs_mem-1]])
        else : cases_voisines.append([-2,-2])
        if ord +1 <= max_ord : cases_voisines.append([(abs,ord+1),mem[ord_mem+1][abs_mem]])
        else : cases_voisines.append([-2,-2])
        min = compteur
        i = 0
        for case in cases_voisines:
            if case[1] != -2 and murs[i] != 1 :
                if case[1] < min:
                    min = case[1]
                    choix = case[0]
            i += 1
        diff_abs = choix[0]-abs
        diff_ord = choix[1]-ord
        color("blue")
        if diff_abs == 1:
            forward(20)
        elif diff_abs == -1:
            backward(20)
        elif diff_ord == 1:
            tp = pos()
            goto(tp[0],tp[1]-20)
        else:
            tp = pos()
            goto(tp[0],tp[1]+20)
        #print("abs: ",abs," ord: ",ord)
        abs = choix[0]
        ord = choix[1]
    #print("abs: ",abs," ord: ",ord)

if __name__ == '__main__':
    (largeur,hauteur,grille) = labyrinthe()
    #print(grille)
    abs_objet  = rand(0,largeur-1)
    ord_objet  = rand(0,hauteur-1)
    abs_reelle = rand(0,largeur-1)
    ord_reelle = rand(0,hauteur-1)
    (mem,mem_laby,abs,ord,min_abs,min_ord,max_abs,max_ord,compteur) = cherche(abs_objet,ord_objet,abs_reelle,ord_reelle,grille,hauteur,largeur)
    retour(mem,mem_laby,abs,ord,min_abs,min_ord,max_abs,max_ord,compteur)
    exitonclick()

