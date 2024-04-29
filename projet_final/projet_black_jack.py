# projet black jack
"""Clément, Théo, Maïwenn"""

from PIL import Image, ImageTk
import random
import tkinter as tk
from PIL import Image, ImageTk  
import time 
import fenetreperdu

resultat = []

def ajouter_au_score(valeur, label):
    label.config(text = f"Score : {valeur}")


def somme_valeurs(cartes):

    '''
    Permet de faire la somme des valeurs des cartes de la main du joueur

    Argument : cartes, la main du joueur, est une liste de tuple  

    Return total, la somme des valeurs
    
    '''
    cartes_nettoyer = nettoyer_cartes(cartes)
    total = 0
    for carte in cartes_nettoyer:
        total += int(carte[2])  # La troisième valeur dans chaque tuple est la valeur numérique
    return total


def redimensionner_image(image, taille):

    '''
    Permet de redimensionner les images des cartes

    Arguments :  image, l'image qu'on veut redimensinner
                 taille, un couple de valeur x, y en pixels à donner à l'image

    Return img_redimensionnee, l'image rentrée mise à la taille souhaitée
    
    '''

    img_pil = Image.open(image)
    img_pil = img_pil.resize(taille)
    img_redimensionnee = ImageTk.PhotoImage(img_pil)
    return img_redimensionnee

def nettoyer_cartes(liste_cartes):

    '''
    Permet de nettoyer la liste car elle contient des [...] entre chaque carte ce qui fausse les index

    Argument :  liste_cartes, une liste avec les cartes distribuées

    Return liste_nettoyee, la liste du début sans les [...]
    
    '''
    liste_nettoyee = []
    for carte in liste_cartes:
        if not isinstance(carte, list):
            liste_nettoyee.append(carte)
    return liste_nettoyee


# generation du paquet de carte 
def jeu_de_carte ():
    '''
    Permet de créer le paquet et d'assigner les valeurs aux cartes 

    Argument :  aucun

    Return rien
    
    '''

    global jeu

    symboles=["trèfle", "coeur", "carreau", "pique"]
    valeurs=["as", "valet", "dame", "roi", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for symbole in symboles:
        for valeur in valeurs:
            if valeur == "valet" or valeur == "dame" or valeur == "roi":
                cartes = (symbole,valeur, 10)
            elif valeur == "as":
                cartes = (symbole, valeur, 1)
            else :
                cartes = (symbole, valeur, int(valeur))
            jeu.append(cartes)


def changement_joueur():

    '''
    Permet de gérer le changement de joueur entre les différents joueurs et le croupier 

    Argument :  aucun

    Return rien 
    
    '''
    global nb_joueur
    global joueur
    
    if joueur == "croupier":
        joueur = 0
    elif joueur < nb_joueur - 1 :
        joueur += 1
    else :
        joueur = "croupier"


# fonction determiner la carte distribué + actualisation du jeu de carte 
def carte_a_distribuer():

    '''
    Permet de distribuer les cartes parmit le paquet et le supprime du jeu

    Argument :  aucun

    Return rien
    
    '''

    global jeu
    global carte
    
    nombre = random.randint(0, len(jeu) - 1)
    carte = jeu[nombre]
    
    jeu.pop(nombre)
    return 

#fonction determiner les carte d'une main et le score 
def main_joueur():


    '''
    Permet de gérer les différentes mains des joueurs et du croupier 

    Argument :  aucun

    Return rien
    
    '''
    global carte
    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    global main_du_croupier
    global score_du_croupier
    
    
    if joueur == "croupier":
        main_du_croupier.append(carte)
        score_du_croupier += carte[2]
    else:
        main_du_joueur = liste_main_du_joueur[joueur]
        score_du_joueur = liste_score_du_joueur[joueur]
        main_du_joueur.append(carte)
        

        score_du_joueur[0] += carte[2]

        liste_main_du_joueur[joueur].append(main_du_joueur)
        liste_score_du_joueur[joueur] = score_du_joueur
    return
    

def carte_en_plus(mainJ_label, canvas, root, score_label, carte_dos):
    '''
    Permet de gérer si le joueur demande une carte en plus et update le canva

    Arguments :  mainJ_label, le texte de la main du joueur
                canvas, une image 
                root, une racine
                score_label, le texte du score 
                carte_dos, l'image d'une carte de dos  

    Return rien
    
    '''
    global jeu
    global carte
    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    score_du_joueur = liste_score_du_joueur[joueur]
    main_du_joueur = liste_main_du_joueur[joueur]

    if score_du_joueur[0] < 21:

        carte_a_distribuer()
        main_joueur()
        
        mainJ_label.config(text = f"main joueur : {main_du_joueur}")
        print(joueur)

        if joueur == 0:
            img03 = "cartes/" + str(carte) + ".gif"  # Chemin d'accès à l'image
            img03_redim = redimensionner_image(img03, (80, 120))
            canvas.create_image(1314, 250, anchor = "nw", image = img03_redim)

        if joueur == 1:
            img13 = "cartes/" + str(carte) + ".gif"
            img13_redim = redimensionner_image(img13, (80, 120))
            canvas.create_image(1134, 380, anchor = "nw", image = img13_redim)

        elif joueur == 2:
            img23 = "cartes/" + str(carte) + ".gif" 
            img23_redim = redimensionner_image(img23, (80, 120))
            canvas.create_image(954, 460, anchor = "nw", image = img23_redim)

        elif joueur == 3:
            img33 = "cartes/" + str(carte) + ".gif"
            img33_redim = redimensionner_image(img33, (80, 120))
            canvas.create_image(727, 495, anchor = "nw", image = img33_redim)

        elif joueur == 4:
            img43 = "cartes/" + str(carte) + ".gif"  
            img43_redim = redimensionner_image(img43, (80, 120))
            canvas.create_image(504, 460, anchor = "nw", image = img43_redim)

        elif joueur == 5:
            img53 = "cartes/" + str(carte) + ".gif" 
            img53_redim = redimensionner_image(img53, (80, 120))
            canvas.create_image(314, 380, anchor = "nw", image = img53_redim)

        elif joueur == 6:
            img63 = "cartes/" + str(carte) + ".gif"  
            img63_redim = redimensionner_image(img63, (80, 120))
            canvas.create_image(154, 250, anchor = "nw", image = img63_redim)
 
        changement_joueur()

        canvas.update()
        canvas.lift() # .lift() permet de forcer tkinter à afficher correctement les cartes, créer aussi une légère erreur peu impactante
        
    canvas.update()
             

def action_croupier():
    '''
    Permet de gérer l'action du croupier, si jamais il a un score de moins de 17, il tire une carte 

    Argument :  aucun

    Return rien
    
    '''

    global jeu
    global carte
    global joueur
    global main_du_croupier
    global score_du_croupier

    while score_du_croupier < 17:

        for i in range (len(main_du_croupier)):
            if main_du_croupier[i][1]=="as":
                if score_du_croupier == 11:
                    main_du_croupier[i]=main_du_croupier[i][0],main_du_croupier[i][1],11
                    score_du_croupier+=10
        carte_a_distribuer()
        main_joueur()
    for i in range (len(main_du_croupier)):
            if main_du_croupier[i][1]=="as":
                main_du_croupier[i]=main_du_croupier[i][0],main_du_croupier[i][1],11
                score_du_croupier+=0
    return 

def valeuras():
    '''
    Permet de demander au joueur possédant un as de choisir sa valeur entre 1 ou 11 dans le terminal

    Argument :  aucun

    Return rien
    
    '''

    global joueur
    global liste_main_du_joueur
    global liste_score_du_joueur
    global choix_as
    main_du_joueur = liste_main_du_joueur[joueur]
    score_du_joueur = liste_score_du_joueur[joueur]

    for i in range (len(main_du_joueur)):
        if main_du_joueur[i][1] == "as":
            valeur_as = int(input("1 ou 11"))
            if valeur_as == 1 or valeur_as == 11 :
                main_du_joueur[i] = (main_du_joueur[i][0], main_du_joueur[i][1], valeur_as)
            else :
                valeur_as = int(input("1 ou 11"))
        score_du_joueur[0] += 10
    return 
def fin_de_jeu():

    '''
    Permet de gérer le résultat des joueurs s'ils ont gagné, perdu, faient une égalité ou bien black jack

    Argument :  aucun

    Return rien 
    
    '''

    global liste_main_du_joueur
    global liste_score_du_joueur
    main_du_joueur = liste_main_du_joueur[joueur]
    score_du_joueur = liste_score_du_joueur[joueur]
    global score_du_croupier
    global resultat

    if somme_valeurs(main_du_joueur) > 21 or somme_valeurs(main_du_joueur) < score_du_croupier and score_du_croupier <= 21 :
        print (somme_valeurs(main_du_joueur))
        print(main_du_joueur)
        print (score_du_croupier)
        print ("perdu")
        resultat.append("perdu")
        print(resultat)

    elif somme_valeurs(main_du_joueur) == 21 and len(main_du_joueur) == 2:
        print (somme_valeurs(main_du_joueur))
        print(main_du_joueur)
        print (score_du_croupier)
        print ("black jack")
        resultat.append("black jack")
        print(resultat)

    elif somme_valeurs(main_du_joueur) == score_du_croupier or somme_valeurs(main_du_joueur) == 21 and somme_valeurs(main_du_joueur) == score_du_croupier :
        print (somme_valeurs(main_du_joueur))
        print(main_du_joueur)
        print (score_du_croupier)
        print ("egalité")
        resultat.append("egalité")
        print(resultat)

    else :
        print (somme_valeurs(main_du_joueur))
        print (score_du_croupier)
        print ("gagner")
        resultat.append("gagner")
        print(resultat)
    

def generation_main_joueur():
    '''
    Permet d'ajouter toutes les mains dans une seule liste 

    Argument :  aucun

    Return liste_main, la liste de toutes les mains des joueurs
    
    '''
    global nb_joueur
    liste_main = []
    for i in range (nb_joueur):
        liste_main.append([])
    print (liste_main)
    return liste_main


def generation_score_joueur():

    '''
    Permet de mettre tous les scores dans une liste 

    Argument :  aucun

    Return liste_score, la liste de tous les scores
    
    '''
    global nb_joueur
    liste_scrore = []
    for i in range (nb_joueur):
        liste_scrore.append([0])
    return liste_scrore