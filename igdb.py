#! /usr/bin/env python3

""" fonctions utiles pour la lecture et l'affichage des fichiers CSV IGDB 
TODO : rien à faire dans ce fichier """

import sys
import csv
import textwrap

def lire_fichier(fichier):
    """Ouvrir un fichier et renvoyer son contenu. """
    try:
        with open(fichier,"r",encoding="utf-8") as flux:    
            texte = flux.read()
            return texte
    except: 
        sys.stderr.write("Impossible d'ouvrir le fichier " +  fichier + "\n")
        sys.exit(1)

def lire_csv(path):
    """Renvoyer les données d'un fichier csv sous forme de listes de lignes. 
    Hypothèses : fichier structuré à l'aide du séparateur ";" / encodé en utf-8. """
    with open(path, encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=";")
        data = list(lecteur)
        return data

def structurer_jeux(data) : 
    """ Structurer les jeux sous la forme d'une liste de dictionnaires. 
    Chaque jeu doit être associé aux champs présents dans la première ligne du tableau data.
    La fonction renvoie la légende sous forme de liste et une liste de dictionnaires représentant chacun un jeu. """
    legende = data[0]    # liste des champs qui devront être présentes dans le dictionnaire 
    res = []         
    
    for l in range (1, len(data)): 
        # l parcourt les lignes à partir de la numéro 1 (donc les jeux)
        game = {}
        for i in range (0, len(data[l])) :
            if legende[i] == "annee" or legende[i] == "mois" or legende[i] == "id_jeu" : 
                game[legende[i]] = int(data[l][i])
            else :
                game[legende[i]] = data[l][i]
        res.append(game)
    return legende,res


def extraire_donnees(chemin, taille = None) : 
    """ Lire un fichier csv dont le chemin est passé en paramètre, 
    le structurer sous forme de listes de dictionnaires, 
    extraire et renvoyer une liste de taille cases ou la liste complète si taille vaut None. """

    data = lire_csv(chemin)
    champs_legende,data_games = structurer_jeux(data)
    
    if taille is not None: 
        return data_games[:taille]
    else : 
        return data_games


def tronquer(texte, largeur=20):
    """Limiter un texte à 20 caractères."""

    texte = str(texte) if texte is not None else ""
    texte = " ".join(texte.split())

    if len(texte) > largeur:
        return texte[:largeur-3] + "..."

    return texte

def afficher_data_tabulaire(indice, data):
    """Afficher les valeurs de chaque dictionnaire, précédées de leur indice. """

    largeur = 15
    ligne = [
        tronquer(str(valeur), largeur).ljust(largeur)
        for valeur in data.values()
    ]
    print(f" {indice:<{6}} | ", end="")
    print(" | ".join(ligne))

def afficher_legende_tabulaire(data):
    """Afficher tous les champs de la légende (les clés de l'objet data) sur une seule ligne."""

    largeur = 15
    ligne = [
        tronquer(str(valeur), largeur).ljust(largeur)
        for valeur in data.keys()
    ]
    print(f" #      | ", end="")
    print(" | ".join(ligne))


def afficher_data_ligne(indice, data):
    """Afficher les valeurs de chaque dictionnaire, précédées de leur indice."""

    largeur = 15
    print(f"\nJeu n° {indice}", end=" # ")

    for champ, valeur in data.items():
        print(f"{champ} : {valeur}", end=" # ")

def afficher_legende_ligne(data):
    """N'affiche rien (inutile puisque afficher_data_fiche présente les champs)"""

def afficher_jeux_tabulaire (L): 
    """ Afficher tous les jeux de la liste L dans un affichage tabulé. """
    afficher_legende_tabulaire(L[0])
    for i,j in enumerate(L) : 
        afficher_data_tabulaire(i,j)

def afficher_fiche(jeu, largeur=80):
    """Afficher une fiche de jeu en s'adaptant à ses propriétés. """

    largeur_champ = max(len(str(champ)) for champ in jeu)
    largeur = max(largeur, largeur_champ + 20)

    print("\n" + "=" * largeur)
    print(f"  {jeu.get('nom_jeu', 'Fiche du jeu')}")
    print("=" * largeur)

    for champ, valeur in jeu.items():
        prefixe = f"{champ:<{largeur_champ}} : "
        texte = "" if valeur is None else str(valeur)

        lignes = textwrap.wrap(
            texte,
            width=largeur - len(prefixe),
            break_long_words=False,
            break_on_hyphens=False
        ) or [""]

        print(prefixe + lignes[0])

        for ligne in lignes[1:]:
            print(" " * len(prefixe) + ligne)

    print("=" * largeur)



if __name__ == "__main__":
    # NB : ce programme doit être invoqué depuis la racine du projet 
    # Puisque les chemins des fichiers à ouvrir sont exprimés par le chemin relatif IGDB/...

    data = lire_csv("IGDB/jeux_consoles.csv")
    #data = lire_csv("IGDB/jeux_toutes_plateformes.csv")
    champs_legende,data_games = structurer_jeux(data)
    print(champs_legende)
    print("Entrees :", len(data_games))
    
    if len(data_games) >0 : 
        afficher_legende(data_games[0])
        for i in range(0,5) :
            afficher_data(i,data_games[i])

    indice = int(input("Saisir indice du jeu à afficher > "))
    if indice >=0 and indice <= len(data_games) :
        afficher_fiche(data_games[indice])
    