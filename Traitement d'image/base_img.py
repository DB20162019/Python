#fichier de "base" pour le triatement d'image

# -*- coding: utf-8 -*-
import PIL.Image as image
import numpy as np


#permet d'enregistrer une image en N&B,
#m est un tableau de pixels
#nom est une chaine de carractéres du nom complet (avec extension) du fichier
def save_img(m,nom): 
    n=len(m)
    p=len(m[0])
    m = np.reshape(m,n*p)
    dam_mb = image.new('L',(n,p))
    dam_mb.putdata(m)
    #dam_mb.show()
    dam_mb.save(nom)

