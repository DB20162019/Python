# -*- coding: utf-8 -*-
def creer_pile():
        return[] 

def empiler(v,p):
	p.append(v)

def depiler(p):
	if len(p)!=0:
                return p.pop()

def taille(p):
	return len(p)

def est_vide(p):
	return taille(p)==0	

def sommet(p):
	assert taille(p)!=0
	return p[-1]

def afficher_pile(p):
        print('sommet')
        i=len(p)
        while i>0:
                i-=1
                print('| ',p[i],' |')
