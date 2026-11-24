#! /usr/bin/env python3

"""
Implémentation des fonctions puissance rapide (indienne) en itératif et en récursif
"""

from my_plot import *
import math 

nb_operations = 0

def puissance_rapide(x, n):
    global nb_operations

    resultat = 1
    while n > 0 :
        if n % 2 == 1: 
            nb_operations += 1
            resultat *= x
            n -= 1

        nb_operations += 1
        x = x*x
        n = n>>1	# équivalent à n=n//2

    return resultat


def puissance_rapide_rec(x,n):
    global nb_operations

    # cas de base 
    if n==0:
        return 1

    # cas général
    if (n%2):  # impair
        nb_operations += 1
        resultat = puissance_rapide_rec(x*x, (n-1) // 2)
        nb_operations += 1
        return x * resultat 
    else:  	# pair
        nb_operations += 1    
        return puissance_rapide_rec(x*x, n//2)




def benchmark(exposant_max,nombre_pas=20): 
    """Mesure les performances des fonctions `puissance` 
    On fait nombre_pas calculs, par défaut 20 """
    global nb_operations

    pas = max(1,exposant_max//nombre_pas)
    values_abs = []
    values_ord = []
    
    for p in range(0,exposant_max+1, pas):
        nb_operations = 0
        puissance_rapide(2,p)
        values_abs.append(p)
        values_ord.append(nb_operations)
    add_plot(values_abs,values_ord, "Puissance rapide itérative","*")

    values_abs = []
    values_ord = []
    for p in range(0,exposant_max+1, pas):
        nb_operations = 0
        puissance_rapide_rec(2,p)
        values_abs.append(p)
        values_ord.append(nb_operations)
    add_plot(values_abs,values_ord, "Puissance rapide récursive")

    values_abs = []
    values_ord = []
    for p in range(1,exposant_max+1, pas):
        values_abs.append(p)
        values_ord.append(1 + math.log2(p))
    add_plot(values_abs,values_ord, "Log2","")

    values_abs = []
    values_ord = []
    for p in range(1,exposant_max+1, pas):
        values_abs.append(p)
        values_ord.append(2 + 2 * math.log2(p))
    add_plot(values_abs,values_ord, "2 x Log2","")

    write_plot("puissances_rapides.png","exposant", "opérations", "Complexité des puissances rapides")

def debordement(exposant_max,nombre_pas=20):
    """Mise en évidence du problème induit par un trop grand nombre de récursions """
    
    pas = max(1,exposant_max//nombre_pas)

    for p in range(0,exposant_max+1, pas): 
        print("2 ^ ", p, " = ", puissance_rapide(2,p))
        print("2 ^ ", p, " = ", puissance_rapide_rec(2,p))

if __name__ == "__main__":
    benchmark(1000,200)
    debordement(1000,5)

    