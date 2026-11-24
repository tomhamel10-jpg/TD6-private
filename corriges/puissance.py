#! /usr/bin/env python3

"""
Implémentation des fonctions puissance en itératif et en récursif
"""

from my_plot import *

nb_operations = 0

def puissance(x, n):
    global nb_operations
    resultat = 1

    if n == 0:
        return 1

    resultat = x 
    for i in range(2, n+1):
        nb_operations += 1 
        resultat *= x

    return resultat

def puissance_rec(x,n):
    global nb_operations

    #cas de base 
    if n == 0:
        return 1

    #cas général
    resultat = puissance_rec(x,n-1)
    nb_operations += 1
    return x * resultat



def benchmark(exposant_max,nombre_pas=20): 
    """Mesure les performances des fonctions `puissance` 
    On fait nombre_pas calculs, par défaut 20 """
    global nb_operations

    pas = max(1,exposant_max//nombre_pas)
    values_abs = []
    values_ord = []
    
    for p in range(0,exposant_max+1, pas):
        nb_operations = 0
        puissance(2,p)
        values_abs.append(p)
        values_ord.append(nb_operations)
        
    add_plot(values_abs,values_ord, "Puissance itérative","*")

    values_abs = []
    values_ord = []
    for p in range(0,exposant_max+1, pas):
        nb_operations = 0
        puissance_rec(2,p)
        values_abs.append(p)
        values_ord.append(nb_operations)
        
    add_plot(values_abs,values_ord, "Puissance récursive")
    write_plot("puissances.png","exposant", "opérations", "Complexité des puissances simples")

def debordement(exposant_max,nombre_pas=20):
    """Mise en évidence du problème induit par un trop grand nombre de récursions """
    
    pas = max(1,exposant_max//nombre_pas)

    for p in range(0,exposant_max+1, pas): 
        print("2 ^ ", p, " = ", puissance(2,p))
        print("2 ^ ", p, " = ", puissance_rec(2,p))

if __name__ == "__main__":
    benchmark(100,20)
    debordement(1000,5)

    