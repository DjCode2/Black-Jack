#fonction.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import FctBlackJack
import json


banque_joueur=0
score=0
mainJ = ""

def quitter_menu(root_menu):
    root_menu.quit()


def ajouter_au_score(nouvelle_valeur, label):
    # Récupérer la valeur actuelle du score depuis le label
    score_actuel = int(label.cget("text").split(":")[1].strip())
    
    nouveau_score = score_actuel + nouvelle_valeur
    label.config(text=f"Score : {nouveau_score}")


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
    root_jeu.destroy()

def demander_carte():#remplace action_joueur
    pass
    
def doubler_mise(score_label):#mise variable global? + ajouter variable banque_joueur qui sera la totalité des jetons disponibles 
    
    pass


def garder_main():
    pass

def abandonner(root_jeu):
    if messagebox.askokcancel("oh la ptite bite", "Êtes-vous sûr de vouloir abandonner ?"):
        root_jeu.destroy()

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

    # Ajouter un bouton "Demander Carte" avec la même couleur de fond que l'image de fond
    demander_button = ttk.Button(root_jeu, text="Demander Carte", command=demander_carte, style="Custom.TButton")
    demander_button.pack()

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

    btn_abandonner = tk.Button(root_jeu, text="Abandonner", width=13, font=("Arial", 15),command=lambda: abandonner(root_jeu))
    btn_abandonner.place(x=1275, y=760)

    btn_demande_carte = tk.Button(root_jeu, text="Demander carte(s)", width=15, font=("Arial", 14), command=demander_carte)
    btn_demande_carte.place(x=470, y=750)

    btn_double_mise = tk.Button(root_jeu, text="Doubler la mise", width=15, font=("Arial", 14), command=lambda:ajouter_au_score(2,score_label))
    btn_double_mise.place(x=650, y=750)

    btn_garder_main = tk.Button(root_jeu, text="Garder la main", width=15, font=("Arial", 14), command=garder_main)
    btn_garder_main.place(x=830, y=750)

    #relatif au jeu --------------------------------------------------

    # programme principale / sera plus tard dans un autre dossier
    jeu=FctBlackJack.jeu_de_carte()
    joueur=FctBlackJack.debut()

    main_du_joueur=[]
    main_du_croupier=[]

    score_du_joueur=0
    score_du_croupier=0


    carte=FctBlackJack.carte_a_distribuer(jeu)
    print(carte[0])
    main=FctBlackJack.main_joueur(carte[0],joueur,main_du_joueur,main_du_croupier,score_du_joueur,score_du_croupier)

    carte2=FctBlackJack.carte_a_distribuer(carte[1])
    print(carte2[0])
    main2=FctBlackJack.main_joueur(carte2[0],main[2],main[3],main[0],main[4],main[1])

    carte3=FctBlackJack.carte_a_distribuer(carte[1])
    print(carte3[0])
    main3=FctBlackJack.main_joueur(carte3[0],main2[2],main2[3],main2[0],main2[4],main2[1])

    carte4=FctBlackJack.carte_a_distribuer(carte[1])
    print(carte4[0])
    main4=FctBlackJack.main_joueur(carte4[0],main3[2],main3[3],main3[0],main3[4],main3[1])

    print(f"main du joueur : {main4[3]} ")#joueur 
    print(f"main du croupier : {main4[0]}" )#croupier

    mainJ_label.config(text=f"main joueur : {main4[3]}")

    root_jeu.mainloop()
