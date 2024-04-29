# projet black jack
"""Clément, Théo, Maïwenn"""

from PIL import Image, ImageTk
import random
import tkinter as tk
from PIL import Image, ImageTk  
import time 
import fenetreperdu


def ajouter_au_score(valeur, label):
    label.config(text=f"Score : {valeur}")

def somme_valeurs(cartes):
    cartes_nettoyer=nettoyer_cartes(cartes)
    total = 0
    for carte in cartes_nettoyer:
        #print(carte[2])
        total += int(carte[2])  # La troisième valeur dans chaque tuple est la valeur numérique
    return total


def redimensionner_image(image, taille):
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
    
    jeu.pop(nombre)
    return 

#fonction determiner les carte d'une main et le score 
def main_joueur():

    global carte
    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    global main_du_croupier
    global score_du_croupier
    
    
    if joueur=="croupier":
        main_du_croupier.append(carte)
        score_du_croupier+=carte[2]
    else:
        main_du_joueur=liste_main_du_joueur[joueur]
        score_du_joueur=liste_score_du_joueur[joueur]
        main_du_joueur.append(carte)
        

        score_du_joueur[0]+=carte[2]

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
        if carte_sup=="carte":
            carte_supplementaire=int(input("saisissez le nombre de carte en plus"))
            for i in range (carte_supplementaire):
                carte_a_distribuer()
                main_joueur()
        else :
            print("error")
    
    return   

def carte_en_plus(mainJ_label,canvas,root,score_label,carte_dos):

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
        
        mainJ_label.config(text=f"main joueur : {main_du_joueur}")
        print(joueur)

        if joueur==0:
            img03 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img03_redim = redimensionner_image(img03, (80, 120))
            canvas.create_image(1314, 250, anchor="nw", image=img03_redim)
            print("pipou carte afi")
        if joueur==1:
            img13 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img13_redim = redimensionner_image(img13, (80, 120))
            canvas.create_image(1134, 380, anchor="nw", image=img13_redim)
            print("pipou carte afi")
        elif joueur==2:
            img23 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img23_redim = redimensionner_image(img23, (80, 120))
            canvas.create_image(954, 460, anchor="nw", image=img23_redim)
            print("pipou carte afi")
        elif joueur==3:
            img33 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img33_redim = redimensionner_image(img33, (80, 120))
            canvas.create_image(727, 495, anchor="nw", image=img33_redim)
            print("pipou carte afi")
        elif joueur==4:
            img43 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img43_redim = redimensionner_image(img43, (80, 120))
            canvas.create_image(504, 460, anchor="nw", image=img43_redim)
            print("pipou carte afi")
        elif joueur==5:
            img53 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img53_redim = redimensionner_image(img53, (80, 120))
            canvas.create_image(314, 380, anchor="nw", image=img53_redim)
            print("pipou carte afi")
        elif joueur==6:
            img63 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img63_redim = redimensionner_image(img63, (80, 120))
            canvas.create_image(154, 250, anchor="nw", image=img63_redim)
            print("pipou carte afi")
        changement_joueur()

        canvas.update()
        canvas.lift()
        
    canvas.update()
    # créé erreur, pas dérengeante pour l'instant, a voir a l'avenir 
    #action_croupier()

    #fin_de_jeu(root)
    
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

def valeuras():

    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    main_du_joueur=liste_main_du_joueur[joueur]
    score_du_joueur=liste_score_du_joueur[joueur]

    for i in range (len(main_du_joueur)):
        if main_du_joueur[i][1]=="as":
            valeur_as=int(input("1 ou 11"))
            if valeur_as==1 or valeur_as==11 :
                main_du_joueur[i]=(main_du_joueur[i][0],main_du_joueur[i][1],valeur_as)
            else :
                valeur_as=int(input("1 ou 11"))
        score_du_joueur[0]+=10
    return 

def fin_de_jeu():

    global liste_main_du_joueur
    global liste_score_du_joueur
    main_du_joueur=liste_main_du_joueur[joueur]
    score_du_joueur=liste_score_du_joueur[joueur]
    global score_du_croupier

    if somme_valeurs(main_du_joueur)>21 or somme_valeurs(main_du_joueur)<score_du_croupier and score_du_croupier<=21 :
        print (somme_valeurs(main_du_joueur))
        print(main_du_joueur)
        print (score_du_croupier)
        print ("perdu")
        #time.sleep(5)
        #fenetreperdu.creer_fenetre_perdu(root,"perdu")
    elif somme_valeurs(main_du_joueur)==21 and len(main_du_joueur)==2:
        print (somme_valeurs(main_du_joueur))
        print(main_du_joueur)
        print (score_du_croupier)
        print ("black jack")
        #time.sleep(5)
        #fenetreperdu.creer_fenetre_perdu(root, "gagner, black jack ! ")
    elif somme_valeurs(main_du_joueur)==score_du_croupier or somme_valeurs(main_du_joueur)==21 and somme_valeurs(main_du_joueur)==score_du_croupier :
        print (somme_valeurs(main_du_joueur))
        print(main_du_joueur)
        print (score_du_croupier)
        print ("egalité")
        #time.sleep(5)
        #fenetreperdu.creer_fenetre_perdu(root, "fait une egalité")
    else :
        print (somme_valeurs(main_du_joueur))
        print (score_du_croupier)
        print ("gagner")
        #time.sleep(5)
        #fenetreperdu.creer_fenetre_perdu(root,"gagner")
    
    return 

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
