# APP 2026-2027 -- TD5

## Support de cours

[Support de cours au format Google docs](https://docs.google.com/presentation/d/1JLU9jKFxe4QtOYGRDouI6OHtLsFNqDkU8vVeB2AuOGo)

## Objectifs du TD 

- Notations asymptotiques de Landau, classes de complexité
- Approche “Diviser pour régner”
- Résolution d’équations de récurrence
- Développement de fonctions récursives, expression des équations de coût

## Utilisation de gnuplot

Le fichier `gnuplot/classes.gp` présente la production de courbes représentant les différentes classes de comportement asymptotique à l'aide de la commande `gnuplot`. 

- Pour produire une image à l'aide de la commande `gnuplot`, il faut taper la commande `gnuplot classes.gp`. 
- Ce programme produit deux diagrammes représentant le comportement des fonctions `log(x)`, `x`, `x * log(x)`, `x^2` et `2^x` pour des valeurs de x de 0 à 100 et de 0 à 500. 

## Exercice 1 : fonction puissance 

Cet exercice utilise le fichier `puissance.py`.

1. Analyser la fonction `puissance` en itératif : quelle est sa complexité ?
- Ecrire le code de l’exponentiation rapide en récursif dans la fonction `puissance_rec`
- Ecrire l’équation de coût et la résoudre par le théorème maître
- Quel problème se présente lorsque l’on calcule des puissances trop grandes avec la version récursive ?


## Exercice 2: exponentiation rapide

Cet exercice utilise le fichier `puissance_rapide.py`.

2. Analyser la fonction `puissance_rapide` en itératif : quelle est sa complexité ? 
- Ecrire le code de l’exponentiation rapide en récursif dans la fonction `puissance_rapide_rec`
- Ecrire l’équation de coût et la résoudre par le théorème maître


## Exercice 3 : recherche dichotomique 

Cet exercice utilise le fichier `recherche_dichotomique.py`. 

3. Analyser la fonction `recherche_dichotomique` en itératif : quelle est sa complexité ?
- Ecrire le  code de la recherche dichotomique en récursif dans la fonction `recherche_dichotomique_rec`
- Ecrire l’équation de coût et la résoudre par le théorème maître
- La résoudre par substitution



