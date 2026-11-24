#! /usr/bin/env python3

"""
Implémentation du tri fusion de listes pythons et de listes chaînées
"""

import random
import math
import sys
import time
from TAD.listes_simplement_chainees import *
from igdb import *
from my_plot import *

nb_comparaisons = 0
nb_affectations = 0
nb_comparaisons_listes = 0
nb_affectations_listes = 0

def init_list_aleatoire(taille) : 
    """initialise une liste de taille entiers aléatoirement """
    L = []
    for i in range(taille):
        L.append(random.randint(1,taille))
    return L

def comparer_generique(e1,e2,cle=None): 
    """ Renvoie une valeur positive si e1>=e2
    On peut se contenter de renvoyer e1-e2 : en effet si e1>=e2; e1-e2>=0
    NB : attention à la nature du champ ! 
    On peut comparer des chaines avec les opérateurs habituels, 
    mais on ne peut pas en faire la soustraction... 
    Si cle est None, on compare directement les elements """

    # TODO: rien à faire

    if cle is None : 
        return e1-e2
    else : 
        return e1[cle]-e2[cle]


def comparer_ids(e1,e2) :
    """ TODO: Comparer deux jeux à partir de leur champ id_jeu """ 

def comparer_annees(e1,e2) : 
    """ TODO: Comparer deux jeux à partir de leur champ annee """

def comparer_mois(e1,e2) : 
    """ TODO: Comparer deux jeux à partir de leur champ mois """

def comparer_noms(e1,e2) : 
    """ TODO: Comparer deux jeux à partir de leur champ nom_jeu """
    nom1 = e1["nom_jeu"].lower()
    nom2 = e2["nom_jeu"].lower()
    
################# TRI FUSION DE LISTES PYTHON ################# 

def est_triee(L,fn_comparaison):
    """ TODO: renvoie True si L (liste python) est triée par ordre croissant du point de vue de la fonction de comparaison utilisée """
    return False
        
def tri_fusion(T, debut, fin,fn_comparaison): 
    # TODO : rien à faire

    if (debut < fin) :
        milieu = (debut + fin)//2
        tri_fusion(T, debut, milieu,fn_comparaison)
        tri_fusion(T, milieu + 1, fin,fn_comparaison)
        fusionner(T, debut, milieu, fin,fn_comparaison)

def fusionner(T, d, m, f,fn_comparaison):
    # TODO : ajouter le comptage des comparaisons et opérations de réorganisation

    global nb_affectations
    global nb_comparaisons

    aux = T[d:f+1].copy() 				    # Copie des éléments à fusionner
    i = 0
    j = m - d + 1
    k = 0
    while i <= m - d and j <= f - d: 		# Fusion des deux parties triées
        if  fn_comparaison(aux[i],aux[j]) <= 0:		
            T[d + k] = aux[i]; i += 1		# aux[i] est plus petit : on le place dans t
        else:
            T[d + k] = aux[j] ; j += 1		# aux[j] est plus petit : on le place dans t
        k += 1

    while i <= m - d:					    # Recopie des éléments restants de la partie gauche
        T[d+k] = aux[i]; i += 1; k += 1

    while j <= f - d:					    # Recopie des éléments restants de la partie droite
        T[d+k] = aux[j]; j += 1; k += 1

################# TRI FUSION DE LISTES CHAINEES ################# 

def liste_est_triee(L,fn_comparaison):
    """ TODO: renvoie True si L (liste chainee) est triée par ordre croissant 
    du point de vue de la fonction de comparaison utilisée """
    return False

def creer_liste_chainee(L, nom, fn_legende, fn_data) :
    """ Insère les éléments d'une liste python dans une liste chainée, en gardant le même ordre. 
    On insère donc en tête dans la liste chainee en commençant par la fin de la liste python """

    # TODO: rien à faire

    LC = ListeChainee(nom, fn_legende, fn_data)
    for e in range(len(L)-1,-1,-1): 
        LC.inserer_tete(L[e])
    return LC

def milieu(cell) : 
    """ Renvoie un pointeur vers le milieu de la liste chainée """
    global nb_affectations_listes
    lent = cell
    if lent.suivant is not None :
        rapide = lent.suivant
        # nb_affectations_listes += 1

    while rapide is not None and rapide.suivant is not None: 
        # nb_affectations_listes += 2
        lent = lent.suivant
        rapide = rapide.suivant.suivant

    return lent

def tri_fusion_liste_chainee(tete,fn_comparaison): 
    """ Tri fusion de listes chainees. Ici, il ne faut plus échanger mais chainer """

    # TODO: rien à faire 

    global nb_affectations_listes
    global nb_comparaisons_listes

    if tete is not None and tete.suivant is not None: 
        # Au moins deux cellules : on peut trouver un milieu
        m = milieu(tete)

        # On coupe en deux à partir du milieu
        droite = m.suivant
        m.suivant = None 
        nb_affectations_listes += 1 

        # On trie récursivement chaque liste 
        gauche = tri_fusion_liste_chainee(tete,fn_comparaison)
        droite = tri_fusion_liste_chainee(droite,fn_comparaison)
        # return fusionner_listes_chainees(gauche,droite,fn_comparaison) # version itérative
        return fusionner_listes_chainees_rec(gauche,droite,fn_comparaison) # version récursive
    else : 
        return tete

def fusionner_listes_chainees_rec(cell1,cell2,fn_comparaison):
    """ TODO : Fusionner deux listes triées pour produire une liste globalement triée
    De manière récursive ! """

    global nb_comparaisons_listes
    global nb_affectations_listes

    # ordre de récurrence ?

    # cas de base ?

    # cas général ? 

    # TODO : Code à supprimer ! 
    # En attendant le code, on fusionne sans organiser quoi que ce soit... 
    fin1 = cell1
    if fin1 is not None: 
        while fin1.suivant is not None:
            fin1 = fin1.suivant
    fin1.suivant = cell2
    # Fin code à supprimer ! 

    return cell1


def fusionner_listes_chainees(cell1, cell2,fn_comparaison):
    """ TODO: Fusionner deux listes chaînées triées pour produire une liste globalement triée
    De manière itérative ! """

    global nb_comparaisons_listes
    global nb_affectations_listes

    # TODO : Code à supprimer ! 
    # En attendant le code, on fusionne sans organiser quoi que ce soit... 
    fin1 = cell1
    if fin1 is not None: 
        while fin1.suivant is not None:
            fin1 = fin1.suivant
    fin1.suivant = cell2
    # Fin code à supprimer ! 

    return cell1


################# BENCHMARK ################# 

def benchmark(L, nom_liste, taille_max,nombre_pas=20, fn_comparaison=None): 
    """Mesure les performances des fonctions `tri_fusion` sur les données de la liste python L """
    
    global nb_affectations
    global nb_comparaisons
    global nb_affectations_listes
    global nb_comparaisons_listes

    if len(L) < taille_max : 
        sys.stderr.write("La liste fournie est trop petite !\n")
        return 

    if fn_comparaison is None: 
        fn_comparaison = comparer_generique

    pas = max(1,taille_max//nombre_pas)
    values_abs = []
    values_ord_comparaisons = []
    values_ord_affectations = []
    values_ord_duree = []
    values_ord_comparaisons_listes = []
    values_ord_affectations_listes = []
    values_ord_duree_listes = []
    nombre_essais = 1   # On peut faire plusieurs essais si chaque essai est différent, mais ce n'est pas le cas ici 

    for n in range(1,taille_max+1, pas):
        nb_affectations = 0
        nb_comparaisons = 0
        nb_affectations_listes = 0
        nb_comparaisons_listes = 0
        duree = 0
        duree_listes = 0
        for essai in range(0,nombre_essais):
            L1 = L[:n].copy()
            L2 = creer_liste_chainee(L1,nom_liste, afficher_legende_tabulaire, afficher_data_tabulaire)
            debut = time.perf_counter()
            tri_fusion(L1, 0, n-1,fn_comparaison)
            fin = time.perf_counter()
            duree += 1000 * (fin - debut)

            debut = time.perf_counter()
            L2.tete = tri_fusion_liste_chainee(L2.tete, fn_comparaison)
            fin = time.perf_counter()
            duree_listes += 1000 * (fin - debut)
            
        values_abs.append(n)
        values_ord_duree.append(duree/ nombre_essais)
        values_ord_duree_listes.append(duree_listes/ nombre_essais)
        values_ord_comparaisons.append(nb_comparaisons/ nombre_essais)
        values_ord_affectations.append(nb_affectations/ nombre_essais)
        values_ord_comparaisons_listes.append(nb_comparaisons_listes/ nombre_essais)
        values_ord_affectations_listes.append(nb_affectations_listes/ nombre_essais)

    add_plot(values_abs,values_ord_comparaisons, "Tri fusion : comparaisons","*")
    add_plot(values_abs,values_ord_affectations, "Tri fusion : affectations","*")
    add_plot(values_abs,values_ord_comparaisons_listes, "Tri fusion de listes : comparaisons","+")
    add_plot(values_abs,values_ord_affectations_listes, "Tri fusion de listes : affectations","+")

    values_abs = []
    values_ord = []
    for n in range(1,taille_max+1, pas):
        values_abs.append(n)
        values_ord.append( n  * math.log2(n))
    add_plot(values_abs,values_ord, "n x Log2(n)","")

    write_plot("fusion.png","taille liste à trier", "comparaisons|reorganisations", "Complexité du tri fusion pour la liste '" + nom_liste+"'")

    add_plot(values_abs,values_ord_duree, "Tri fusion : duree","*")
    add_plot(values_abs,values_ord_duree_listes, "Tri fusion de listes : duree","+")
    write_plot("durees_fusion.png","taille liste à trier", "durée (ms)", "Tri fusion pour la liste '" + nom_liste+"'")



if __name__ == "__main__":
    
    # Partie 1 : tri fusion de listes d'entiers python  #################
    # 1) ajouter à tri_fusion le comptage des opérations et comparaisons
    # 2) implémenter la fonction est_triee
    # 3) tester et conclure en observant la courbe générée

    taille = 10000
    L = init_list_aleatoire(taille)
    print("est trié ?", est_triee(L,comparer_generique))

    nb_affectations = 0
    nb_comparaisons = 0
    tri_fusion(L, 0, len(L)-1,comparer_generique)

    print("Affectations :", nb_affectations, "comparaisons : ", nb_comparaisons)
    print("est trié ?", est_triee(L,comparer_generique))

    benchmark(L, "liste d'entiers", taille,20) 
    # on ne fournit pas de fonction de comparaison : comparer_generique sera utilisée

    # Partie 2 : tests sur des listes python de jeux #################

    #L = extraire_donnees("IGDB/jeux_consoles.csv", 10) # 10 éléments
    #L = extraire_donnees("IGDB/jeux_consoles.csv") # toute la liste !
    #L = extraire_donnees("IGDB/jeux_toutes_plateformes.csv", 10) # 10 éléments
    #L = extraire_donnees("IGDB/jeux_toutes_plateformes.csv") # toute la liste !

    #afficher_jeux_tabulaire(L)

    # TODO : Comment la liste est-elle triée au départ ?
    # trier pour déterminer si le tri est stable
    # Quelle est la complexité pratique du tri des jeux ?


    # Partie 3 : tri fusion de listes chainees #################

    #L = extraire_donnees("IGDB/jeux_consoles.csv") # toute la liste !
    #L = extraire_donnees("IGDB/jeux_toutes_plateformes.csv") # toute la liste !

    #L2 = creer_liste_chainee(L, "Jeux console", afficher_legende_tabulaire, afficher_data_tabulaire)  # affichage tabulaire tronqué
    #L2 = creer_liste_chainee(L, "Jeux console", afficher_legende_ligne, afficher_data_ligne) # affichage intégral sur une ligne 

    #L2.afficher()

    #L2.tete = tri_fusion_liste_chainee(L2.tete,comparer_mois)
    #print("Liste est triée par mois ?", liste_est_triee(L2,comparer_mois))

    #L2.tete = tri_fusion_liste_chainee(L2.tete,comparer_annees)
    #print("Liste est triée par annee ?", liste_est_triee(L2,comparer_annees))
    
    #L2.afficher()

    #i = int(input("Quel jeu souhaitez-vous afficher ? (saisir son indice, pas son id) > "))
    #afficher_fiche(L2.acces(i).valeur)
