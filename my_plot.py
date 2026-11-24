from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def add_plot (data_abs, data_ord,label_courbe, marqueur="x"): 
    # ajoute un tracé dans le futur graphique en mémoire 
    """ Marqueur	Forme
        "o"	        Cercle
        "s"	        Carré
        "^"	        Triangle vers le haut
        "v"	        Triangle vers le bas
        "*"	        Étoile
        "+"	        Plus
        "x"	        Croix
        "D"	        Losange
        "."	        Petit point
        "None"	    Aucun marqueur """

    plt.plot(data_abs, data_ord, marker=marqueur, label=label_courbe)
    plt.legend()
    plt.grid()

    

def write_plot(filename, label_x, label_y, titre): 
    # produit une courbe à partir des données du graphique en mémoire, 
    # stockée dans le fichier indiqué par l'argument filename

    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(titre)
    fichier = Path(__file__).with_name(filename)
    plt.savefig(fichier)
    print(f"Graphique enregistré dans : {fichier}")
    plt.close()