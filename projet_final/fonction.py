#fonction.py
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import projet_black_jack
import param
import time
import subprocess


banque_joueur=0
score=0
mainJ = ""
joueur_joue=False
compt_carte_sup = 0



def affiche_carte_croup (canvas,carte_dos):
    '''
    Permet d'afficher les cartes du croupier 

    Argument :  canvas, le fond du jeu
                carte_dos, la carte retourner du croupier 

    Return liste_nettoyee, la liste du début sans les [...]
    
    '''
    canvas.delete(carte_dos)
    img9croup = "cartes/" + str(projet_black_jack.main_du_croupier[1]) + ".gif"  # Chemin d'accès à l'image
    img9_redim_croup = projet_black_jack.redimensionner_image(img9croup, (80, 120))
    canvas.create_image(700, 290, anchor="nw", image=img9_redim_croup)
    canvas.update()
    return 



   
def quitter_menu(root_menu):
    '''
    Permet de quitter la fenetre

    Argument :  root_menu, la fenetre de lancement du jeu

    Return rien
    
    '''
    root_menu.quit()

def quitter(root_jeu):
    '''
    Permet de quitter le jeu

    Argument :  root_jeu, la fenetre de jeu

    Return rien
    
    '''
    if messagebox.askokcancel("black jack juge you", "Êtes-vous sûr de vouloir quitter ? "):
        root_jeu.destroy()

def doubler_mise(mise_label, mise, root_jeu,canvas,img_dos):#mise variable global? + ajouter variable banque_joueur qui sera la totalité des jetons disponibles 
    '''
    Permet de doubler la mise mise en jeu

    Arguments :  mise_label, le texte avec la mise
                mise, la valeur de la mise
                root_jeu, la fenetre de jeu
                canvas, les images
                img_dos, la carte retourner

    Return rien
    
    ''' 
    projet_black_jack.joueur
    param.mise = mise*2 
    mise_label.configure(text=f"Mise: {mise*2}")
    projet_black_jack.changement_joueur()
    print (projet_black_jack.joueur)

    return

def abandonner(mise_label,mise,canvas,img_dos,root_jeu): 
    '''
    Permet d'abandonner la partie et de récupérer la moitié de sa mise'

    Arguments :  mise_label, le texte avec la mise
                mise, la valeur de la mise
                root_jeu, la fenetre de jeu
                canvas, les images
                img_dos, la carte retourner

    Return rien
    
    '''    
    projet_black_jack.joueur
    param.mise = mise/2
    mise = mise/2
    mise_label.configure(text=f"Mise: {mise}")
    projet_black_jack.changement_joueur()
    print (projet_black_jack.joueur)
    
    return 

def garder_main(mise_label,mise,canvas,img_dos,root_jeu): 
    '''
    Permet de garder sa main donc passer son tour 

    Arguments :  mise_label, le texte avec la mise
                mise, la valeur de la mise
                root_jeu, la fenetre de jeu
                canvas, les images
                img_dos, la carte retourner

    Return rien
    
    '''
    projet_black_jack.joueur
    mise_label.configure(text=f"Mise: {mise}")
    #affiche_carte_croup(canvas,img_dos)
    projet_black_jack.changement_joueur()
    print (projet_black_jack.joueur)
    
    return 


def demander_carte(mainJ_label,canvas,root_jeu,score_label,img_dos):
    '''
    Permet de demander une carte en plus si nous le désirons

    Arguments :  mainJ_label, le texte avec la main du joueur
                root_jeu, la fenetre de jeu
                canvas, les images
                img_dos, la carte retourner
                score_label, le texte du score

    Return rien
    
    '''    
    projet_black_jack.joueur
    print (projet_black_jack.joueur)
    #affiche_carte_croup (canvas,img_dos)
    projet_black_jack.carte_en_plus(mainJ_label,canvas,root_jeu,score_label,img_dos)
    return 

def BouclePrincipale(root_menu):
    '''
    Permet de gérer le jeu

    Argument :  root_menu, la fenetre de menu

    Return rien
    
    ''' 
    # Fermer la fenêtre de menu
    global action
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

    #crée boutons et label
    mainJ_label = tk.Label(root_jeu, text=f"main joueur: {mainJ}", font=("Arial", 16))
    score_label = tk.Label(root_jeu, text=f"Score: {score}", font=("Arial", 16))
    mise_label = tk.Label(root_jeu, text=f"Mise: {param.mise} AR$", font=("Arial", 16))
    btn_quit = tk.Button(root_jeu, text="Quitter", width=13, font=("Arial", 15), command=lambda: quitter(root_jeu))
    
    #les placer 
    score_label.place(x=20, y=20)  
    mise_label.place(x=20, y=60) 
    mainJ_label.place(x=500, y=700)  
    btn_quit.place(x=1282, y=8)

    #relatif au jeu --------------------------------------------------



    # distribution 

    #projet_black_jack.nb_joueur = param.nb_joueurs

    # programme principale 
    projet_black_jack.jeu=[]
    projet_black_jack.carte=0 
    projet_black_jack.joueur=0
    projet_black_jack.nb_joueur= param.nb_joueurs
    projet_black_jack.mainjoueurpnj = []

    projet_black_jack.liste_main_du_joueur=projet_black_jack.generation_main_joueur()
    projet_black_jack.main_du_joueur=[] 
    projet_black_jack.main_du_croupier=[]

    projet_black_jack.liste_score_du_joueur=projet_black_jack.generation_score_joueur()
    projet_black_jack.score_du_joueur=0
    projet_black_jack.score_du_croupier=0

    valeur_possible=[1260,1080,900,673,450,260,100]
    valeur_possible2=[250,380,460,495,460,380,250]


    print(f"nb joueur maiwan : {projet_black_jack.nb_joueur}")
    print(f"nb joueur maiwan : {projet_black_jack.nb_joueur}")

    projet_black_jack.jeu_de_carte()
    for i in range (projet_black_jack.nb_joueur+1):
        print (projet_black_jack.joueur)
        projet_black_jack.carte_a_distribuer()
        projet_black_jack.main_joueur()
        print (projet_black_jack.carte)

        if projet_black_jack.joueur=="croupier":
            img_croup_01 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img_redim_croup_01 = projet_black_jack.redimensionner_image(img_croup_01, (80, 120))
            canvas.create_image(673, 290, anchor="nw", image=img_redim_croup_01)

        elif projet_black_jack.joueur==0 :
            #affichage carte
            img01 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img01_redim = projet_black_jack.redimensionner_image(img01, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img01_redim)
        
        elif projet_black_jack.joueur==1 :
            #affichage carte
            img11 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img11_redim = projet_black_jack.redimensionner_image(img11, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img11_redim)
       
        elif projet_black_jack.joueur==2 :
            #affichage carte
            img21 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img21_redim = projet_black_jack.redimensionner_image(img21, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img21_redim)
        
        elif projet_black_jack.joueur==3 :
            #affichage carte
            img31 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img31_redim = projet_black_jack.redimensionner_image(img31, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img31_redim)
        
        elif projet_black_jack.joueur==4 :
            #affichage carte
            img41 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img41_redim = projet_black_jack.redimensionner_image(img41, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img41_redim)
        
        elif projet_black_jack.joueur==5 :
            #affichage carte
            img51 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img51_redim = projet_black_jack.redimensionner_image(img51, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img51_redim)
        
        elif projet_black_jack.joueur==6 :
            #affichage carte
            img61 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img61_redim = projet_black_jack.redimensionner_image(img61, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur], valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img61_redim)
        
        if projet_black_jack.joueur!="croupier":
            #ajouter au score 
            projet_black_jack.ajouter_au_score(projet_black_jack.somme_valeurs(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[projet_black_jack.joueur])),score_label)
            #debug sur jeu direct
            mainJ_label.config(text=f"main joueur : {projet_black_jack.liste_main_du_joueur[projet_black_jack.joueur]}")
        
        canvas.update()
        time.sleep(2)
        projet_black_jack.changement_joueur()
    
    for i in range (projet_black_jack.nb_joueur+1):
        print (projet_black_jack.joueur)
        projet_black_jack.carte_a_distribuer()
        projet_black_jack.main_joueur()
        print (projet_black_jack.carte)

        if projet_black_jack.joueur=="croupier":
            img_dos_croup = "cartes/" + "dos_carte" + ".png"  # Chemin d'accès à l'image
            img_dos_redim_croup = projet_black_jack.redimensionner_image(img_dos_croup, (80, 120))
            canvas.create_image(700, 290, anchor="nw", image=img_dos_redim_croup )

        elif projet_black_jack.joueur==0 :
            #affichage carte
            img02 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img02_redim = projet_black_jack.redimensionner_image(img02, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img02_redim)
        
        elif projet_black_jack.joueur==1 :
            #affichage carte
            img12 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img12_redim = projet_black_jack.redimensionner_image(img12, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img12_redim)
        
        elif projet_black_jack.joueur==2 :
            #affichage carte
            img22 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img22_redim = projet_black_jack.redimensionner_image(img22, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img22_redim)
        
        elif projet_black_jack.joueur==3 :
            #affichage carte
            img32 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img32_redim = projet_black_jack.redimensionner_image(img32, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img32_redim)
        
        elif projet_black_jack.joueur==4 :
            #affichage carte
            img42 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img42_redim = projet_black_jack.redimensionner_image(img42, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img42_redim)
        
        elif projet_black_jack.joueur==5 :
            #affichage carte
            img52 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img52_redim = projet_black_jack.redimensionner_image(img52, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img52_redim)
        elif projet_black_jack.joueur==6 :
            #affichage carte
            img62 = "cartes/" + str(projet_black_jack.carte) + ".gif"  # Chemin d'accès à l'image
            img62_redim = projet_black_jack.redimensionner_image(img62, (80, 120))
            canvas.create_image(valeur_possible[projet_black_jack.joueur]+27, valeur_possible2[projet_black_jack.joueur], anchor="nw", image=img62_redim)
        
            #print(projet_black_jack.main_du_joueur)
        if projet_black_jack.joueur!="croupier":
            #ajouter au score 
            projet_black_jack.ajouter_au_score(projet_black_jack.somme_valeurs(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[projet_black_jack.joueur])),score_label)
            #debug sur jeu direct
            mainJ_label.config(text=f"main joueur : {projet_black_jack.liste_main_du_joueur[projet_black_jack.joueur]}")
            
        canvas.update()
        time.sleep(2)
        projet_black_jack.changement_joueur()
    
    def suite ():
        projet_black_jack.joueur=0
        for a in range (projet_black_jack.nb_joueur):
            projet_black_jack.valeuras()
            projet_black_jack.changement_joueur()
            print("pipou")
            canvas.update()

        # affichage de la main du croupier
        projet_black_jack.main_du_croupier
        projet_black_jack.action_croupier()
        print(projet_black_jack.main_du_croupier)

        #afficher 1ere carte croupie 
        img_croup_02 = "cartes/" + str(projet_black_jack.main_du_croupier[1]) + ".gif"
        img_redim_croup_02 = projet_black_jack.redimensionner_image(img_croup_02, (80, 120))
        canvas.create_image(700, 290, anchor="nw", image=img_redim_croup_02)
        canvas.update()

        if len(projet_black_jack.main_du_croupier)>2:
            img_croup_03 = "cartes/" + str(projet_black_jack.main_du_croupier[2]) + ".gif"
            img_redim_croup_03 = projet_black_jack.redimensionner_image(img_croup_03, (80, 120))
            canvas.create_image(754, 290, anchor="nw", image=img_redim_croup_03) 

        if len(projet_black_jack.main_du_croupier)>3:
            img_croup_04= "cartes/" + str(projet_black_jack.main_du_croupier[3]) + ".gif"
            img_redim_croup_04 = projet_black_jack.redimensionner_image(img_croup_04, (80, 120))
            canvas.create_image(781, 290, anchor="nw", image=img_redim_croup_04)

        if len(projet_black_jack.main_du_croupier)>4:
            img_croup_05 = "cartes/" + str(projet_black_jack.main_du_croupier[4]) + ".gif"
            img_redim_croup_05 = projet_black_jack.redimensionner_image(img_croup_05, (80, 120))
            canvas.create_image(808, 290, anchor="nw", image=img_redim_croup_05)

        canvas.update()
        projet_black_jack.joueur=0

        for b in range (projet_black_jack.nb_joueur):
            projet_black_jack.fin_de_jeu()
            projet_black_jack.changement_joueur()

        canvas.update()
        canvas.lift() 
        return
    
        
    btn_abandonner = tk.Button(root_jeu, text="Abandonner", width=13, font=("Arial", 15),command=lambda: abandonner(mise_label, param.mise, canvas,img_dos_redim_croup,root_jeu))
    btn_abandonner.place(x=1050, y=750)#recup la moitié de la mise et retour maison 

    btn_demande_carte = tk.Button(root_jeu, text="Demander carte(s)", width=15, font=("Arial", 14), command=lambda:demander_carte(mainJ_label,canvas,root_jeu,score_label,img_dos_redim_croup))
    btn_demande_carte.place(x=470, y=750)

    btn_double_mise = tk.Button(root_jeu, text="Doubler la mise", width=15, font=("Arial", 14), command=lambda:doubler_mise(mise_label, param.mise, root_jeu,canvas,img_dos_redim_croup))
    btn_double_mise.place(x=650, y=750)

    btn_garder_main = tk.Button(root_jeu, text="Garder la main", width=15, font=("Arial", 14), command=lambda: garder_main(mise_label, param.mise, root_jeu,canvas,img_dos_redim_croup))
    btn_garder_main.place(x=830, y=750)

    btn_garder_main = tk.Button(root_jeu, text="valider", width=15, font=("Arial", 14), command=suite)
    btn_garder_main.place(x=200, y=700)

    btn_garder_main = tk.Button(root_jeu, text="Fin du Jeu", width=15, font=("Arial", 14), command=lambda:creer_fenetre_perdu(root_jeu,projet_black_jack.resultat))
    btn_garder_main.place(x=200, y=750)

    canvas.update()    
    
    #debug main du joueur 
    print(f"la main du joueur : {projet_black_jack.liste_main_du_joueur[0]}")  
    print (f"la main de jack black {projet_black_jack.main_du_croupier}")
    
    print(projet_black_jack.liste_main_du_joueur[0])

    root_jeu.mainloop()

def creer_fenetre_perdu(root,resultat):

    resultattest = ["gagné","Perdu","gagné","gagné","Perdu","Perdu","gagné"]
    # Fonction appelée lorsque le bouton est cliqué

    def Rejouer(root):
        root.destroy()
        fenetre.destroy()
        subprocess.call(["python", "mainloop.py"]) #eviter les imports circulaires

    def quitter(root):
        fenetre.destroy()
        root.destroy()
    
    # Créer la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("resultat")

    fenetre.geometry("450x520")

    # Étiquette avec le message "Vous avez perdu"
    if param.nb_joueurs >=1:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 1 à  {projet_black_jack.resultat[0]}", font=("Arial", 16))
        etiquette1.pack(pady=5)
    
    if param.nb_joueurs >=2:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 2 à  {projet_black_jack.resultat[1]}", font=("Arial", 16))
        etiquette1.pack(pady=5)

    if param.nb_joueurs >=3:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 3 à  {projet_black_jack.resultat[2]}", font=("Arial", 16))
        etiquette1.pack(pady=5)

    if param.nb_joueurs >=4:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 4 à  {projet_black_jack.resultat[3]}", font=("Arial", 16))
        etiquette1.pack(pady=5)

    if param.nb_joueurs >=5:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 5 à  {projet_black_jack.resultat[4]}", font=("Arial", 16))
        etiquette1.pack(pady=5)

    if param.nb_joueurs >=6:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 6 à  {projet_black_jack.resultat[5]}", font=("Arial", 16))
        etiquette1.pack(pady=5)

    if param.nb_joueurs >=7:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 7 à  {projet_black_jack.resultat[6]}", font=("Arial", 16))
        etiquette1.pack(pady=5)


    # Étiquette avec le message de la mise
    mise_label = tk.Label(fenetre, text=f"Votre mise était de {param.mise} AR$", font=("Arial", 12))
    mise_label.pack(pady=15)

    # Bouton "Quitter"
    rejouer_btn = tk.Button(fenetre, text="Rejouer", width=14, font=("Arial", 25), bg="green", command=lambda: Rejouer(root))
    rejouer_btn.pack(pady=5)
    bouton_quitter = tk.Button(fenetre, text="Quitter", width=14, font=("Arial", 25), bg="red", command=lambda: quitter(root))
    bouton_quitter.pack(pady=5)


    # Boucle principale de la fenêtre
    fenetre.mainloop()


#    . 　　　。　　　　•　 　ﾟ　　。 　　。 .   .
#　　　.　　　 　　.　　　　　。　　　.  　 。 . 。
#.　　 。   　•　　　 .   ඞ 。 . 　　 • 　　　　•
#　　ﾟ　　 Jack Black was not An Impostor.　 。　.
#　　'　　。    　1 Impostor remains 　    　 。
#　　ﾟ　　　.　　　. ,　　　　.　 .   .    • 　。 . 
#　 　.　　　 .　 .   . 　　　。　　　.  　 。 . 。
