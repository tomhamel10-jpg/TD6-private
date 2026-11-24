#! /usr/bin/env python3

"""
Implémentation du problème des tours de Hanoï
"""

import random
import math
from my_plot import *

nb_operations = 0

def hanoi(colonne_depart, colonne_destination, colonne_intermediaire, nombre_disques, show=True):

    # Cas de base
    if nombre_disques == 1:
        if show: 
            print(f"{colonne_depart} => {colonne_destination}")
        return 1

    # Cas général
    i = hanoi(colonne_depart, colonne_intermediaire, colonne_destination, nombre_disques - 1)
    i += hanoi(colonne_depart, colonne_destination, colonne_intermediaire, 1)
    i += hanoi(colonne_intermediaire, colonne_destination, colonne_depart, nombre_disques - 1)

    return i

def benchmark(taille_max,nombre_pas=20): 
    """Mesure les performances de la fonction `hanoi` 
   pour un nombre de disques croissant """
    global nb_operations

    pas = max(1,taille_max//nombre_pas)
    values_abs = []
    values_ord = []
    nombre_essais = 20
    
    for n in range(1,taille_max+1, pas):
        values_abs.append(n)
        values_ord.append(hanoi('A','B','C', n, False))
        
    add_plot(values_abs,values_ord, "Tours de Hanoi","*")

    values_abs = []
    values_ord = []
    for n in range(1,taille_max+1, pas):
        values_abs.append(n)
        values_ord.append(2**n)
    add_plot(values_abs,values_ord, "2^n","+")

    write_plot("hanoi.png","nombre de disques", "deplacements", "Complexité de la résolution des tours de Hanoï")


if __name__ == "__main__":
    hanoi('col 1', 'col 2', 'col 3', 4)
    benchmark(10, 10)
    

    