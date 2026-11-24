# APP 2026-2027 -- TP6

## Support de cours

[Support de cours au format Google docs](https://docs.google.com/presentation/d/1XcBpPvsIFBGWx2rMuEK5Jt9ogOvH3MpEpn1W6HkCKuU/edit?usp=sharing)

## Objectifs du TP

- Utiliser des fonctions de rappel 
- Implémenter un tri fusion de listes Python
- Implémenter un tri fusion de listes chaînées
- Expérimenter les tris sur un jeu de données réel comportant plusieurs clés
- Tracer les courbes de complexité de ces fonctions pour vérifier leurs complexités théoriques


## Exercice 1 : Présentation du code fourni

Le programme `igdb.py` permet de lire et structurer les données du jeu de données extraites du site [IGDB](https://www.igdb.com/) (Internet Game Database). 

Il contient les fonctions suivantes :

- `extraire_donnees(chemin_fichier_csv, nombre_a_extraire)` : permet d'extraire les données depuis un fichier CSV.
- `afficher_jeux_tabulaire(L)` : permet d'afficher une liste de jeux au format tabulaire, à l'aide des fonctions :
  - `afficher_legende_tabulaire(data_jeu)` : affiche la légende des données.
  - `afficher_data_tabulaire(data_jeu)` : affiche les données d'un jeu.
- `afficher_fiche(data_jeu, largeur_affichage)` : affiche une fiche détaillée d'un jeu

D'autres fonctions sont proposées pour présenter les jeux sous forme d'une suite de ligne contenant des informations complètes plutôt que formatée en tableau : 
  - `afficher_legende_ligne(data_jeu)` : affiche la légende des données.
  - `afficher_data_ligne(data_jeu)` : affiche les données d'un jeu.

Deux fichiers de données sont fournis, extraits de la base IGDB à raison d'une entrée maximum par jeu, ciblant uniquement les jeux associés à la région `worldwide` et disposant d'une année et d'un mois de sortie : 

- `IGDB/jeux_consoles.csv` : contient 44 375 entrées.
- `IGDB/jeux_toutes_plateformes.csv` : contient 220 130 entrées.


1. Tester le programme `igdb.py` sur les fichiers `jeux_consoles.csv` et `jeux_toutes_plateformes.csv`.
2. Afficher une fiche de jeu de votre choix.

## Exercice 2 : Fonction de rappel pour les listes simplement chaînées

Les listes simplement chaînées du TD3/TP4 implémentées dans le fichier `TAD/listes_simplement_chainees.py` ont été refactorisées  : leur constructeur `ListeChainee(nom, fn_legende, fn_data)` permet de créer des listes chaînées génériques en utilisant des fonctions de rappel pour l'affichage de leurs éléments.

3. Implémenter les fonctions de callback suivantes :
- `afficher_legende_simple` qui doit afficher `affichage par callback`.
- `afficher_data_simple` qui doit afficher `(indice) data ->`.

4. Tester le fichier `TAD/listes_simplement_chainees.py`.

## Exercice 3 : Tri fusion de listes Python

Les fonctions à implémenter et compléter se trouvent dans le fichier `tri_fusion.py`.

### 3.1 Fonctions de comparaison

5. Implémenter les fonctions de comparaison proposées dans le fichier :

- `comparer_ids(e1, e2)`
- `comparer_annees(e1, e2)`
- `comparer_mois(e1, e2)`
- `comparer_noms(e1, e2)`

Une fonction de comparaison doit renvoyer :

- `0` si les deux éléments sont égaux selon le critère de comparaison.
- Un nombre négatif si le premier élément est considéré comme inférieur au second.
- Un nombre positif si le premier élément est considéré comme supérieur au second.

6. Implémenter également la fonction `est_trie(L, fn_comparaison)`, qui permet de vérifier si une liste Python est intégralement triée en utilisant une fonction de comparaison passée en paramètre.

### 3.2 Implémentation du tri fusion sur des listes python

La fonction `tri_fusion(T, debut, fin, fn_comparaison)` est déjà écrite. Il faut comprendre son fonctionnement et l'utilisation de la fonction de rappel `fn_comparaison`.

La fonction `fusionner(T, d, m, f, fn_comparaison)` permet de fusionner deux sous-listes triées. Il faut y ajouter les variables de comptage permettant de produire les courbes de complexité : 
- `nb_comparaisons` comptabilise les comparaisons effectuées
- `nb_affectations` comptabilise les opérations de réorganisation

### 3.3 Tests et analyse de complexité

7. Tester le tri fusion sur des listes d'entiers générées par la fonction `init_list_aleatoire(taille)`.
- Vérifier que la liste est correctement triée.
- Vérifier que les compteurs ont évolué.
- Étudier la complexité pratique du tri à l'aide de la fonction `benchmark(L, nom_liste, taille_max, nombre_pas, fn_comparaison)`.

8. Tester également le tri fusion sur une liste de jeux vidéo :
- Déterminer comment la liste est triée initialement.
- Vérifier si le tri fusion est stable.
- Étudier la complexité pratique du tri des jeux à l'aide de la fonction `benchmark`. 

## Exercice 4 : Tri fusion de listes chaînées

Le tri fusion de listes chaînées est également à implémenter dans `tri_fusion.py`. Les fonctions `milieu(cell)` et `tri_fusion_liste_chainee(tete, fn_comparaison)` sont déjà fournies. Il faut comprendre leur fonctionnement et leur utilisation.

9. Implémenter les fonctions suivantes : 
- `liste_est_triee(L, fn_comparaison)` : permet de vérifier si une liste chaînée est intégralement triée.
- `fusionner_listes_chainees_rec(cell1, cell2, fn_comparaison)` : fusionne deux listes chaînées triées de manière récursive.
- `fusionner_listes_chainees(cell1, cell2, fn_comparaison)` : fusionne deux listes chaînées triées de manière itérative.

10. Tester et comparer les résultats obtenus à l'aide de chacune de ces fonctions à l'aide de la fonction de benchmark. 

## Conclusion – GTA

11. Pour conclure le TP, trier la liste complète des jeux vidéo successivement par mois et annee, puis l'afficher sur la sortie standard de votre programme
- Filtrer ensuite cette sortie pour extraire les lignes contenant les chaînes `Grand Theft Auto` et `PS`, puis enregistrer le résultat dans le fichier `gta.txt` à l'aide de la commande :

```bash
./prog | grep "Grand Theft Auto" | grep "PS" > gta.txt
```
- Consulter le fichier généré `gta.txt` et déterminer les dates de sortie des jeux GTA sur PlayStation.


