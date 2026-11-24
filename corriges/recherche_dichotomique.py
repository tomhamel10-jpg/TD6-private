#! /usr/bin/env python3

"""
Implémentation de la recherche dichotomique
"""

import random
import math
from my_plot import *

nb_operations = 0

def comparaison(e1,e2): 
    # Renvoie une valeur positive si e1>=e2
    # On peut se contenter de renvoyer e1-e2 : en effet si e1>=e2; e1-e2>=0
    return e1-e2

def recherche_dichotomique(T, e):
    global nb_operations 
    
    # On recherche l'élément e dans la liste T
    debut = 0
    fin = len(T) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        test = comparaison(e, T[milieu])
        nb_operations += 1
        if test == 0:
            # trouvé ! 
            return milieu
        if test < 0:
            # on cherche à gauche car e est < elt du milieu 
            fin = milieu - 1
        else :
            # on cherche à droite 
            debut = milieu + 1

    # lorsque debut>fin, on a inversé les bornes : l'élément n'a pas été trouvé
    return None	# e n’est pas dans T / ne pas renvoyer False 
    # car on pourrait le confondre avec l'indice 0

def recherche_dichotomique_rec(T, debut, fin, e):

    global nb_operations

     # Cas de base : tableau vide
    if fin-debut < 0:
        return None

    # Cas général
    milieu = (fin+debut) // 2

    # Comparaison de l'élément recherché avec T[milieu]
    test = comparaison(e, T[milieu])
    nb_operations += 1

    if test == 0:
        return milieu

    elif test < 0:
        # Recherche dans la première moitié
        return recherche_dichotomique_rec(T, debut, milieu-1, e)

    else:
        # Recherche dans la deuxième moitié
        return recherche_dichotomique_rec(T, milieu+1,fin,e)


def init_list_aleatoire(taille) : 
    # initialise une liste triée aléatoirement
    # on procède par "sauts" en ajoutant une petite valeur aléatoire à chaque fois
    # les sauts font au minimum 2 pour qu'il soit facile de générer une valeur appartenant au tableau 
    # comme un valeur ne lui appartenant pas (en ajoutant simplement +1 à une valeur qui existe)
    # rappel : random.randint(a,b) génère que valeur entre a et b COMPRIS
    L = []
    derniere_valeur = 0
    for i in range(taille):
        derniere_valeur += random.randint(2, 10)
        L.append(derniere_valeur)

    present = L[random.randint(0,len(L)-1)]
    absent = L[random.randint(0,len(L)-1)]  + 1 
    return L, present, absent

def benchmark(taille_max,nombre_pas=20): 
    """Mesure les performances des fonctions `recherche` 
    Dans des tableaux de plus en plus grands 
    Pour chaque taille, on calcule le nombre moyen d'opérations pour trouver l'élément 
    sur N essais """
    global nb_operations

    pas = max(1,taille_max//nombre_pas)
    values_abs = []
    values_ord = []
    nombre_essais = 20
    
    for taille in range(0,taille_max+1, pas):
        nb_operations = 0
        #print("taille: ", taille)
        for essai in range(0,nombre_essais): 
            L,present,absent = init_list_aleatoire(taille+100)  
            # pour ne pas avoir des tableaux trop petits 
            recherche_dichotomique(L,present)
            #print(nb_operations, " ", end="")
        values_abs.append(taille+100)
        values_ord.append(nb_operations // nombre_essais)
        
    add_plot(values_abs,values_ord, "Recherche dichotomique","*")

    values_abs = []
    values_ord = []
    for taille in range(0,taille_max+1, pas):
        nb_operations = 0
        #print("taille: ", taille)
        for essai in range(0,nombre_essais): 
            L,present,absent = init_list_aleatoire(taille+100)  
            # pour ne pas avoir des tableaux trop petits 
            recherche_dichotomique_rec(L,0,len(L)-1,present)
            #print(nb_operations, " ", end="")
        values_abs.append(taille+100)
        values_ord.append(nb_operations // nombre_essais)
        
    add_plot(values_abs,values_ord, "Recherche dichotomique recursive","*")

    values_abs = []
    values_ord = []
    for p in range(1,taille_max+1, pas):
        values_abs.append(p)
        values_ord.append(math.log2(p))
    add_plot(values_abs,values_ord, "Log2","")

    write_plot("recherches.png","taille tableau", "comparaisons", "Complexité de la recherche dichotomique")


if __name__ == "__main__":
    L,present,absent = init_list_aleatoire(100)
    print(L, present , absent)
    print("indice de ", present, " : ", recherche_dichotomique(L,present))
    print("indice de ", absent, " : ", recherche_dichotomique(L,absent))

    print("indice de ", present, " : ", recherche_dichotomique_rec(L,0,len(L)-1, present))
    print("indice de ", absent, " : ", recherche_dichotomique_rec(L,0,len(L)-1,absent))

    benchmark(10000, 100)
    

    