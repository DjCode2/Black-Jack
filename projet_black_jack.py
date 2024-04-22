# projet black jack
"""Clément, Théo, Maïwenn"""

import random
import tkinter as tk
import numpy as np



def ajouter_au_score(valeur, label):
    label.config(text=f"Score : {valeur}")


# generation du paquet de carte 


def jeu_de_carte ():

    global jeu

    symboles=["trèfle","coeur","carreau","pique"]
    valeurs=["as","valet","dame","roi","2","3","4","5","6","7","8","9","10"]
    for symbole in symboles:
        for valeur in valeurs:
            if valeur=="valet" or valeur=="dame" or valeur=="roi":
                cartes=(symbole,valeur,10)
            elif valeur=="as":
                cartes=(symbole,valeur,1)
            else :
                cartes=(symbole,valeur,int(valeur))
            jeu.append(cartes)
    return 

def changement_joueur():

    global joueur

    print(joueur)
    #nombre_de_joueur=int(input("combien de joueur?"))
    #assert nombre_de_joueur<5 and nombre_de_joueur>0
    # numpy array et implementer avec le nombre de joueur donner 
    #ou for de nombre de joueur et crer une list
    if joueur==1: #joueur
        joueur=2 #croupier
    else :
        joueur=1
    return 

# fonction determiner la carte distribué + actualisation du jeu de carte 
def carte_a_distribuer():

    global jeu
    global carte
    
    nombre=random.randint(0,len(jeu))
    carte=jeu[nombre] #bug ici

    if carte[1]=="as":
        valeur_as=int(input("1 ou 11"))
        assert valeur_as==1 or valeur_as==11
        carte_donner2=(carte[0],carte[1],valeur_as)
        carte=carte_donner2
    
    jeu.pop(nombre)
    return 

#fonction determiner les carte d'une main et le score 
def main_joueur():

    global carte
    global joueur
    global main_du_joueur
    global main_du_croupier
    global score_du_joueur
    global score_du_croupier

    if joueur==1:
        main_du_joueur.append(carte)
        score_du_joueur+=carte[2]
    else:
        main_du_croupier.append(carte)
        score_du_croupier+=carte[2]
    return

def somme_valeurs(cartes):
    total = 0
    for carte in cartes:
        total += carte[2]  # La troisième valeur dans chaque tuple est la valeur numérique
    return total

def action_joueur(mainJ_label,score_label):

    global jeu
    global carte
    global joueur
    global main_du_joueur
    global score_du_joueur

    if score_du_joueur<21:
        carte_a_distribuer()
        main_joueur()

        print(main_du_joueur)
        mainJ_label.config(text=f"main joueur : {main_du_joueur}")
        ajouter_au_score(somme_valeurs(main_du_joueur),score_label)
        action_croupier()
        fin_de_jeu()
    else :
        print(2)
    
    return main_du_joueur

def action_croupier():

    global jeu
    global carte
    global joueur
    global main_du_croupier
    global score_du_croupier

    while score_du_croupier<17:
        carte_a_distribuer()
        main_joueur()
    return 

def fin_de_jeu():

    global main_du_joueur
    global score_du_joueur
    global score_du_croupier

    if score_du_joueur>21 or score_du_joueur<score_du_croupier and score_du_croupier<21 :
        print ("perdu")
    elif score_du_joueur==21 and len(main_du_joueur)==2:
        print ("black jack")
    elif score_du_joueur==score_du_croupier or score_du_joueur==21 and score_du_joueur==score_du_croupier :
        print ("egalité")
    else :
        print ("gagner")

# programme principale 
jeu=[]
carte=0 
joueur=1

main_du_joueur=[] 
main_du_croupier=[]

score_du_joueur=0
score_du_croupier=0





#fonction double mise faite 

