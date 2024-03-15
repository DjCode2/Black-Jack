# projet black jack
"""Clément(le meilleur), Théo, Maïwenn"""

import os
try:
    import random
    import tkinter as tk
while 'ImportError':
    os.fork()

tapis = tk.Tk()

# dico des carte pour les avoir en memoire
valeur_as=int(input("1 ou 11"))
assert valeur_as==1 or valeur_as==11

valeur_possible={"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "valet":10, "dame":10, "roi":10, "as":valeur_as}
carte_trefle={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_pique={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_coeur={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_carreau={"2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":1, "valet":1, "dame":1, "roi":1, "as":1}
carte_possible={"2":4, "3":4, "4":4, "5":4, "6":4, "7":4, "8":4, "9":4, "10":4, "valet":4, "dame":4, "roi":4, "as":4}

#fonction pour les joueur
def debut ():
    joueur_debut="joueur1"
    return joueur_debut

def changement_joueur(player):
    #nombre_de_joueur=int(input("combien de joueur?"))
    #assert nombre_de_joueur<5 and nombre_de_joueur>0
    # numpy array et implementer avec le nombre de joueur donner 
    #ou for de nombre de joueur et crer une list
    if player=="joueur":
        player="croupier"
    return player

# fonction determiner la carte distribué 
def carte_a_distribuer(dicoc,dicoc2,dicot,dicop,dicoval):
    symbole=[dicoc,dicoc2,dicot,dicop]
    carte_symbole=random.randint(0,3)

    valeur=[symbole[carte_symbole].keys()]
    carte_valeur=random.randint(0,len(valeur))
    valeur_carte=dicoval[valeur[carte_valeur]]
    # carte donner au joueur utile pour tkinter
    carte_distribuer=(symbole[carte_symbole],valeur_carte)

    return (carte_distribuer,symbole[carte_symbole],valeur[carte_valeur])

# mise a jour dico 
def actualisation_dico(dicov,dicos,v):
    for i in dicos.keys():
        if i==v :
            dicos[i]-=1
            if dicos[i]==0:
                del dicos[i]
                break
    for i in dicov.keys():
        if i==v :
            dicov[i]-=1
            if dicos[i]==0:
                del dicos[i]
                break
    return (dicov,dicos)


carte_joueur1=[]
somme1=sum(carte_joueur1)

carte_croupier=[]
somme1=sum(carte_croupier)


carte_joueur1.append(carte_distribuer)


tapis.mainloop()
