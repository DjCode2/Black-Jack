# projet black jack
"""Clément, Théo, Maïwenn"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk   

def creer_fenetre_perdu(root):
    # Fonction appelée lorsque le bouton est cliqué
    def quitter(root):
        # Afficher une boîte de dialogue pour confirmer la sortie
        fenetre.destroy()
        root.destroy()

    # Créer la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Vous avez perdu")

    # Étiquette avec le message "Vous avez perdu"
    etiquette = tk.Label(fenetre, text="Vous avez perdu")
    etiquette.pack(pady=20)

    # Bouton "Quitter"
    quitter_button = tk.Button(fenetre, text="Quitter", width=10, font=("Arial", 25), bg="red", command= lambda:quitter(root))
    quitter_button.pack()
    # Boucle principale de la fenêtre
    fenetre.mainloop()


def ajouter_au_score(valeur, label):
    label.config(text=f"Score : {valeur}")

def somme_valeurs(cartes):
    total = 0
    for carte in cartes:
        total += carte[2]  # La troisième valeur dans chaque tuple est la valeur numérique
    return total


def redimensionner_image(image, taille):
    """
    Redimensionne une image.

    Args:
        image (tk.PhotoImage): Objet PhotoImage à redimensionner.
        taille (tuple): Taille de l'image redimensionnée au format (largeur, hauteur).

    Returns:
        tk.PhotoImage: Objet PhotoImage redimensionné.
    """
    img_pil = Image.open(image)
    img_pil = img_pil.resize(taille)
    img_redimensionnee = ImageTk.PhotoImage(img_pil)
    return img_redimensionnee




def nettoyer_cartes(liste_cartes):
    liste_nettoyee = []
    for carte in liste_cartes:
        if not isinstance(carte, list):
            liste_nettoyee.append(carte)
    return liste_nettoyee

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

    # numpy array et implementer avec le nombre de joueur donner 
    #ou for de nombre de joueur et crer une list

    global nb_joueur
    global joueur
    
    if joueur=="croupier":
        joueur=0
    elif joueur<nb_joueur-1:
        joueur+=1
    else :
        joueur="croupier"

    return 

# fonction determiner la carte distribué + actualisation du jeu de carte 
def carte_a_distribuer():

    global jeu
    global carte
    
    nombre=random.randint(0,len(jeu)-1)
    carte=jeu[nombre]

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
    global liste_main_du_joueur
    global liste_score_du_joueurscore_du_joueur
    global main_du_croupier
    global score_du_croupier
    x = 673
    

    
    if joueur=="croupier":
        main_du_croupier.append(carte)
        score_du_croupier+=carte[2]
        #print (main_du_croupier)
        #print (score_du_croupier)
    else:
        main_du_joueur=liste_main_du_joueur[joueur]
        score_du_joueur=liste_score_du_joueur[joueur]
        main_du_joueur.append(carte)
        main_du_joueur_netoyer = nettoyer_cartes(main_du_joueur)

        #print(main_du_joueur_netoyer)
        score_du_joueur[0]+=carte[2]
        #print (main_du_joueur)
        #print (score_du_joueur)
        liste_main_du_joueur[joueur].append(main_du_joueur)
        liste_score_du_joueur[joueur]=score_du_joueur
    return

def action_joueur():

    global jeu
    global carte
    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    score_du_joueur=liste_score_du_joueur[joueur]
    main_du_joueur=liste_main_du_joueur[joueur]

    if score_du_joueur[0]<21:
        carte_sup=input("saisissez 'carte' si vous souahiter une carte en plus")
        #assert carte_sup=="carte"
        if carte_sup=="carte":
            carte_supplementaire=int(input("saisissez le nombre de carte en plus"))
            for i in range (carte_supplementaire):
                carte_a_distribuer()
                main_joueur()
        else :
            print("error")
    
    return   

def carte_en_plus(mainJ_label,canvas,root):

    global jeu
    global carte
    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    score_du_joueur=liste_score_du_joueur[joueur]
    main_du_joueur=liste_main_du_joueur[joueur]

    if score_du_joueur[0]<21:

        carte_a_distribuer()
        main_joueur()
        
        #print(main_du_joueur)
        mainJ_label.config(text=f"main joueur : {liste_main_du_joueur[0]}")

        img = "cartes/" + str(nettoyer_cartes(liste_main_du_joueur[0])[-1]) + ".gif"  # Chemin d'accès à l'image
        img_redim = redimensionner_image(img, (80, 120))
        canvas.create_image(730, 495, anchor="nw", image=img_redim)
        print("pipou carte afi")

        action_croupier()
        

    
    fin_de_jeu(root)
    
    return          

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

def fin_de_jeu(root):

    global liste_main_du_joueur
    global liste_score_du_joueur
    main_du_joueur=liste_main_du_joueur[joueur]
    score_du_joueur=liste_score_du_joueur[joueur]
    global score_du_croupier

    if score_du_joueur[0]>21 or score_du_joueur[0]<score_du_croupier and score_du_croupier<=21 :
        print ("perdu")
        creer_fenetre_perdu(root)
    elif score_du_joueur[0]==21 and len(main_du_joueur)==2:
        print ("black jack")
        creer_fenetre_perdu(root)
    elif score_du_joueur[0]==score_du_croupier or score_du_joueur[0]==21 and score_du_joueur[0]==score_du_croupier :
        print ("egalité")
        creer_fenetre_perdu(root)
    else :
        print ("gagner")
        creer_fenetre_perdu(root)

def generation_main_joueur():
    global nb_joueur
    liste_main=[]
    for i in range (nb_joueur):
        liste_main.append([])
    print (liste_main)

    return liste_main

def generation_score_joueur():
    global nb_joueur
    liste_scrore=[]
    for i in range (nb_joueur):
        liste_scrore.append([0])

    return liste_scrore

# programme principale 
jeu=[]
carte=0 
joueur=0
nb_joueur=2

liste_main_du_joueur=generation_main_joueur()
main_du_joueur=[] 
main_du_croupier=[]

liste_score_du_joueur=generation_score_joueur()
score_du_joueur=0
score_du_croupier=0

