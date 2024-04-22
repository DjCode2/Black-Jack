#fonction.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import projet_black_jack
import param
import json

banque_joueur=0
score=0
mainJ = ""

def quitter_menu(root_menu):
    root_menu.quit()

def sauvegarder(score):
    # chopper la date 
    date_heure_actuelles = datetime.datetime.now()
    date_formatee = date_heure_actuelles.strftime("%Y-%m-%d")
    heure_formatee = date_heure_actuelles.strftime("%H:%M:%S")
    
    donnees = {
        "score": score,
        "date": (date_formatee, heure_formatee)
    }
    
    # Enregistrement des données
    with open("donnees.json", "w") as fichier:
        json.dump(donnees, fichier)

def quitter(root_jeu):

    if messagebox.askokcancel("black jack juge you", "Êtes-vous sûr de vouloir quitter ? "):
        root_jeu.destroy()


def doubler_mise(score_label):#mise variable global? + ajouter variable banque_joueur qui sera la totalité des jetons disponibles 
    pass

def affiche_mainJ(mainj,label):

    label.config(text=f"Score : {mainj}")

def BouclePrincipale(root_menu):
    # Fermer la fenêtre de menu
    
    root_menu.destroy()
    root_jeu = tk.Tk()
    root_jeu.title("BlackJack")
    largeur_fenetre_jeu = 1440
    hauteur_fenetre_jeu = 810

    # Charger l'image du tapis de blackjack
    image_tapis = tk.PhotoImage(file="tapis_trool.png")

    # Créer un canvas pour afficher l'image du tapis de blackjack
    canvas = tk.Canvas(root_jeu, width=largeur_fenetre_jeu, height=hauteur_fenetre_jeu)
    canvas.pack()   
    canvas.create_image(0, 0, anchor="nw", image=image_tapis)

    root_jeu.resizable(False, False)
    root_jeu.geometry(f"{largeur_fenetre_jeu}x{hauteur_fenetre_jeu}")


    # Configuration du style pour le bouton
    root_jeu.tk_setPalette(background="#377D22", foreground='white', activeBackground="#377D22", activeForeground='white')
    root_jeu.option_add('*TButton*background', "#377D22")
    root_jeu.option_add('*TButton*foreground', 'white')
    root_jeu.option_add('*TButton*padding', 5)
    root_jeu.option_add('*TButton*relief', 'flat')

    score_label = tk.Label(root_jeu, text=f"Score: {score}", font=("Arial", 16))
    score_label.place(x=20, y=20)  # Ajuster la position selon vos besoins

    mainJ_label = tk.Label(root_jeu, text=f"main joueur: {mainJ}", font=("Arial", 16))
    mainJ_label.place(x=500, y=700)  # Ajuster la position selon vos besoins

    btn_save = tk.Button(root_jeu, text="Sauvegarder", width=13, font=("Arial", 15), command=lambda: sauvegarder(score))
    btn_save.place(x=1282, y=7)

    btn_quit = tk.Button(root_jeu, text="Quitter", width=13, font=("Arial", 15), command=lambda: quitter(root_jeu))
    btn_quit.place(x=1282, y=52)

    btn_abandonner = tk.Button(root_jeu, text="Abandonner", width=13, font=("Arial", 15))
    btn_abandonner.place(x=1275, y=760)#recup la moitié de la mise et retour maison 

    btn_demande_carte = tk.Button(root_jeu, text="Demander carte(s)", width=15, font=("Arial", 14), command=lambda:projet_black_jack.action_joueur(mainJ_label,score_label,canvas))
    btn_demande_carte.place(x=470, y=750)

    btn_double_mise = tk.Button(root_jeu, text="Doubler la mise", width=15, font=("Arial", 14), command=lambda:param.doublemise())
    btn_double_mise.place(x=650, y=750)

    btn_garder_main = tk.Button(root_jeu, text="Garder la main", width=15, font=("Arial", 14), command=projet_black_jack.fin_de_jeu)
    btn_garder_main.place(x=830, y=750)

    #relatif au jeu --------------------------------------------------

    # distribution 
    projet_black_jack.jeu_de_carte()
    for i in range (4):
        projet_black_jack.carte_a_distribuer()
        projet_black_jack.main_joueur()
        projet_black_jack.changement_joueur()

    #debug main du joueur 
    print(f"la main du joueur : {projet_black_jack.main_du_joueur}")  
    print (f"la main de jack black {projet_black_jack.main_du_croupier}")

    #debug sur jeu direct
    mainJ_label.config(text=f"main joueur : {projet_black_jack.main_du_joueur}")

    #ajouter au score 
    projet_black_jack.ajouter_au_score(projet_black_jack.somme_valeurs(projet_black_jack.main_du_joueur),score_label)
    
    # affichage de la main du joueur :
    img1 = "cartes/" + str(projet_black_jack.main_du_joueur[0]) + ".gif"  # Chemin d'accès à l'image
    img2 = "cartes/" + str(projet_black_jack.main_du_joueur[1]) + ".gif"  # Chemin d'accès à l'image

    #redimentionner
    img1_redim = projet_black_jack.redimensionner_image(img1, (80, 120))
    img2_redim = projet_black_jack.redimensionner_image(img2, (80, 120))

    # Afficher les images redimensionnées sur le canevas
    canvas.create_image(673, 495, anchor="nw", image=img1_redim)
    canvas.create_image(700, 495, anchor="nw", image=img2_redim)

    #afficher main croupier 
    img1croup = "cartes/" + str(projet_black_jack.main_du_croupier[0]) + ".gif"  # Chemin d'accès à l'image
    img2croup = "cartes/" + str(projet_black_jack.main_du_croupier[1]) + ".gif"  # Chemin d'accès à l'image

    img1_redim_croup = projet_black_jack.redimensionner_image(img1croup, (80, 120))
    img2_redim_croup = projet_black_jack.redimensionner_image(img2croup, (80, 120))

    # Afficher les images redimensionnées sur le canevas
    canvas.create_image(673, 290, anchor="nw", image=img1_redim_croup)
    canvas.create_image(700, 290, anchor="nw", image=img2_redim_croup)


    root_jeu.mainloop()


#    . 　　　。　　　　•　 　ﾟ　　。 　　。 .   .
#　　　.　　　 　　.　　　　　。　　　.  　 。 . 。
#.　　 。   　•　　　 .   ඞ 。 . 　　 • 　　　　•
#　　ﾟ　　 Jack Black was not An Impostor.　 。　.
#　　'　　。    　1 Impostor remains 　    　 。
#　　ﾟ　　　.　　　. ,　　　　.　 .   .    • 　。 . 
#　 　.　　　 .　 .   . 　　　。　　　.  　 。 . 。
