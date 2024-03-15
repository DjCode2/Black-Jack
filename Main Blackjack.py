# projet black jack
"""Clément(le meilleur), Théo, Maïwenn"""

import random
import tkinter as tk

tapis = tk.Tk()

valeur_as=int(input("1 ou 11"))
assert valeur_as==1 or valeur_as==11

# dico des carte pour les avoir en memoire 
valeur_possible={"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "valet":10, "dame":10, "roi":10, "as":valeur_as}
carte_trefle={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_pique={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_coeur={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_carreau={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}

carte_possible={"2":4, "3":4, "4":4, "5":4, "6":4, "7":4, "8":4, "9":4, "10":4, "valet":4, "dame":4, "roi":4, "as":4}


def joueur_a_determiner():
    pass
    

carte_joueur1=[]
somme1=sum(carte_joueur1)

carte_croupier=[]
somme1=sum(carte_croupier)

# fonction determiner la carte distribué 
def carte_a_distribuer():
    symbole=["trefle", "pique", "coeur", "carreau"]
    carte_symbole=random.randint(0,3)

    valeur=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]
    carte_valeur=random.randint(0,12)

    # carte donner au joueur utile pour tkinter 
    carte_distribuer=(symbole[carte_symbole],valeur[carte_valeur])
    carte_joueur1.append(carte_distribuer)







tapis.mainloop()