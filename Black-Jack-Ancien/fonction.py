#fonction.py
import tkinter as tk
from tkinter import messagebox
import projet_black_jack
import param


banque_joueur=0
score=0
mainJ = ""
joueur_joue = True

compt_carte_sup = 0


def affiche_carte_croup (canvas,carte_dos):
    canvas.delete(carte_dos)
    img2croup = "cartes/" + str(projet_black_jack.main_du_croupier[1]) + ".gif"  # Chemin d'accès à l'image
    img2_redim_croup = projet_black_jack.redimensionner_image(img2croup, (80, 120))
    canvas.create_image(700, 290, anchor="nw", image=img2_redim_croup)


def tour_des_pnj(canvas,carte_dos):#plus tards belec 
    canvas.delete(carte_dos)
    img2croup = "cartes/" + str(projet_black_jack.main_du_croupier[1]) + ".gif"  # Chemin d'accès à l'image
    img2_redim_croup = projet_black_jack.redimensionner_image(img2croup, (80, 120))
    canvas.create_image(700, 290, anchor="nw", image=img2_redim_croup)
   
def quitter_menu(root_menu):
    root_menu.quit()

def quitter(root_jeu):

    if messagebox.askokcancel("black jack juge you", "Êtes-vous sûr de vouloir quitter ? "):
        root_jeu.destroy()

def doubler_mise(mise_label, mise, root_jeu,canvas,img_dos):#mise variable global? + ajouter variable banque_joueur qui sera la totalité des jetons disponibles 
    global joueur_joue
    param.mise = mise*2 
    mise_label.configure(text=f"Mise: {mise*2}")
    joueur_joue = False

    affiche_carte_croup(canvas,img_dos)
    projet_black_jack.fin_de_jeu(root_jeu)

def abandonner(mise_label,mise,canvas,img_dos,root):
    global joueur_joue
    param.mise = mise/2
    mise = mise/2
    mise_label.configure(text=f"Mise: {mise}")
    affiche_carte_croup(canvas,img_dos)
    projet_black_jack.fin_de_jeu(root)
    

    joueur_joue = False

def garder_main(mise_label,mise,canvas,img_dos,root_jeu):
    global joueur_joue
    mise_label.configure(text=f"Mise: {mise}")
    affiche_carte_croup(canvas,img_dos)
    joueur_joue = False
    projet_black_jack.fin_de_jeu(root_jeu)


def demander_carte(mainJ_label,canvas,root_jeu,score_label,img_dos):
    joueur_joue = False

    affiche_carte_croup (canvas,img_dos)
    projet_black_jack.carte_en_plus(mainJ_label,canvas,root_jeu,score_label,img_dos)
    projet_black_jack.fin_de_jeu(root_jeu)

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

    mise_label = tk.Label(root_jeu, text=f"Mise: {param.mise}", font=("Arial", 16))
    mise_label.place(x=20, y=60)  # Ajuster la position selon vos besoins

    mainJ_label = tk.Label(root_jeu, text=f"main joueur: {mainJ}", font=("Arial", 16))
    mainJ_label.place(x=500, y=700)  # Ajuster la position selon vos besoinsSZ

    btn_quit = tk.Button(root_jeu, text="Quitter", width=13, font=("Arial", 15), command=lambda: quitter(root_jeu))
    btn_quit.place(x=1282, y=8)

    btn_abandonner = tk.Button(root_jeu, text="Abandonner", width=13, font=("Arial", 15),command=lambda: abandonner(mise_label, param.mise, canvas,img_dos_redim_croup,root_jeu))
    btn_abandonner.place(x=1050, y=750)#recup la moitié de la mise et retour maison 

    btn_demande_carte = tk.Button(root_jeu, text="Demander carte(s)", width=15, font=("Arial", 14), command=lambda:demander_carte(mainJ_label,canvas,root_jeu,score_label,img_dos_redim_croup))
    btn_demande_carte.place(x=470, y=750)

    btn_double_mise = tk.Button(root_jeu, text="Doubler la mise", width=15, font=("Arial", 14), command=lambda:doubler_mise(mise_label, param.mise, root_jeu,canvas,img_dos_redim_croup))
    btn_double_mise.place(x=650, y=750)

    btn_garder_main = tk.Button(root_jeu, text="Garder la main", width=15, font=("Arial", 14), command=lambda: garder_main(mise_label, param.mise, root_jeu,canvas,img_dos_redim_croup))
    btn_garder_main.place(x=830, y=750)

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

    print(f"nb joueur maiwan : {projet_black_jack.nb_joueur}")
    print(f"nb joueur maiwan : {projet_black_jack.nb_joueur}")

    projet_black_jack.jeu_de_carte()
    for i in range (projet_black_jack.nb_joueur*2+2):
        projet_black_jack.carte_a_distribuer()
        projet_black_jack.main_joueur()
        #print(projet_black_jack.main_du_joueur)
        projet_black_jack.changement_joueur()


    #debug main du joueur 
    print(f"la main du joueur : {projet_black_jack.liste_main_du_joueur[0]}")  
    print (f"la main de jack black {projet_black_jack.main_du_croupier}")

    #debug sur jeu direct
    mainJ_label.config(text=f"main joueur : {projet_black_jack.liste_main_du_joueur[0]}")

    #ajouter au score 
    projet_black_jack.ajouter_au_score(projet_black_jack.somme_valeurs(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[0])),score_label)
    print(projet_black_jack.liste_main_du_joueur[0])
 
    # affichage de la main du joueur : --------------
    img1 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[0])[0]) + ".gif"  # Chemin d'accès à l'image
    img2 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[0])[1]) + ".gif"  # Chemin d'accès à l'image

    #redimentionner
    img1_redim = projet_black_jack.redimensionner_image(img1, (80, 120))
    img2_redim = projet_black_jack.redimensionner_image(img2, (80, 120))

    # Afficher les images redimensionnées sur le canevas
    canvas.create_image(673, 495, anchor="nw", image=img1_redim)
    canvas.create_image(700, 495, anchor="nw", image=img2_redim)

    #afficher main croupier 
    img1croup = "cartes/" + str(projet_black_jack.main_du_croupier[0]) + ".gif"  # Chemin d'accès à l'image
    img1_redim_croup = projet_black_jack.redimensionner_image(img1croup, (80, 120))

    img_dos_croup = "cartes/" + "dos_carte" + ".png"  # Chemin d'accès à l'image
    img_dos_redim_croup = projet_black_jack.redimensionner_image(img_dos_croup, (80, 120))
    # Afficher les images redimensionnées sur le canevas
    canvas.create_image(673, 290, anchor="nw", image=img1_redim_croup)
    canvas.create_image(700, 290, anchor="nw", image=img_dos_redim_croup)
   
   


    if projet_black_jack.nb_joueur >= 2 : 
        # affichage de la main du 2 eme joueur : --------------
        img1pnj1 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[1])[0]) + ".gif"  # Chemin d'accès à l'image
        img2pnj1 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[1])[1]) + ".gif"  # Chemin d'accès à l'image

        #redimentionner
        img1_redim_pnj1 = projet_black_jack.redimensionner_image(img1pnj1, (80, 120))
        img2_redim_pnj1 = projet_black_jack.redimensionner_image(img2pnj1, (80, 120))

        # Afficher les images redimensionnées sur le canevas
        canvas.create_image(900, 460, anchor="nw", image=img1_redim_pnj1)
        canvas.create_image(927, 460, anchor="nw", image=img2_redim_pnj1)

    if projet_black_jack.nb_joueur >= 3 : 
        # affichage de la main du 3 eme joueur : --------------
        img1pnj2 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[2])[0]) + ".gif"  # Chemin d'accès à l'image
        img2pnj2 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[2])[1]) + ".gif"  # Chemin d'accès à l'image

        #redimentionner
        img1_redim_pnj2 = projet_black_jack.redimensionner_image(img1pnj2, (80, 120))
        img2_redim_pnj2 = projet_black_jack.redimensionner_image(img2pnj2, (80, 120))

        # Afficher les images redimensionnées sur le canevas
        canvas.create_image(450, 460, anchor="nw", image=img2_redim_pnj2)
        canvas.create_image(487, 460, anchor="nw", image=img1_redim_pnj2)
        

    if projet_black_jack.nb_joueur >= 4 : 
        # affichage de la main du 3 eme joueur : --------------
        img1pnj3 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[3])[0]) + ".gif"  # Chemin d'accès à l'image
        img2pnj3 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[3])[1]) + ".gif"  # Chemin d'accès à l'image

        #redimentionner
        img1_redim_pnj3 = projet_black_jack.redimensionner_image(img1pnj3, (80, 120))
        img2_redim_pnj3 = projet_black_jack.redimensionner_image(img2pnj3, (80, 120))

        # Afficher les images redimensionnées sur le canevas
        canvas.create_image(1080, 380, anchor="nw", image=img1_redim_pnj3)
        canvas.create_image(1107, 380, anchor="nw", image=img2_redim_pnj3)
        

    if projet_black_jack.nb_joueur >= 5 : 
        # affichage de la main du 3 eme joueur : --------------
        img1pnj4 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[4])[0]) + ".gif"  # Chemin d'accès à l'image
        img2pnj4 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[4])[1]) + ".gif"  # Chemin d'accès à l'image

        #redimentionner
        img1_redim_pnj4 = projet_black_jack.redimensionner_image(img1pnj4, (80, 120))
        img2_redim_pnj4 = projet_black_jack.redimensionner_image(img2pnj4, (80, 120))

        # Afficher les images redimensionnées sur le canevas
        canvas.create_image(260, 380, anchor="nw", image=img1_redim_pnj4)
        canvas.create_image(287, 380, anchor="nw", image=img2_redim_pnj4)

    if projet_black_jack.nb_joueur >= 6 : 
        # affichage de la main du 3 eme joueur : --------------
        img1pnj5 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[5])[0]) + ".gif"  # Chemin d'accès à l'image
        img2pnj5 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[5])[1]) + ".gif"  # Chemin d'accès à l'image

        #redimentionner
        img1_redim_pnj5 = projet_black_jack.redimensionner_image(img1pnj5, (80, 120))
        img2_redim_pnj5 = projet_black_jack.redimensionner_image(img2pnj5, (80, 120))

        # Afficher les images redimensionnées sur le canevas
        canvas.create_image(1260, 250, anchor="nw", image=img1_redim_pnj5)
        canvas.create_image(1287, 250, anchor="nw", image=img2_redim_pnj5)

    if projet_black_jack.nb_joueur >= 7 : 
        # affichage de la main du 3 eme joueur : --------------
        img1pnj6 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[5])[0]) + ".gif"  # Chemin d'accès à l'image
        img2pnj6 = "cartes/" + str(projet_black_jack.nettoyer_cartes(projet_black_jack.liste_main_du_joueur[5])[1]) + ".gif"  # Chemin d'accès à l'image

        #redimentionner
        img1_redim_pnj6 = projet_black_jack.redimensionner_image(img1pnj6, (80, 120))
        img2_redim_pnj6 = projet_black_jack.redimensionner_image(img2pnj6, (80, 120))

        # Afficher les images redimensionnées sur le canevas
        canvas.create_image(100, 250, anchor="nw", image=img1_redim_pnj6)
        canvas.create_image(127, 250, anchor="nw", image=img2_redim_pnj6)
    
    if joueur_joue == False : 
        #ici on fera joueur les IA, joeur_joue sera false quand le joueur aura fini de joueur
        print("le joueur a joué")



    root_jeu.mainloop()


#    . 　　　。　　　　•　 　ﾟ　　。 　　。 .   .
#　　　.　　　 　　.　　　　　。　　　.  　 。 . 。
#.　　 。   　•　　　 .   ඞ 。 . 　　 • 　　　　•
#　　ﾟ　　 Jack Black was not An Impostor.　 。　.
#　　'　　。    　1 Impostor remains 　    　 。
#　　ﾟ　　　.　　　. ,　　　　.　 .   .    • 　。 . 
#　 　.　　　 .　 .   . 　　　。　　　.  　 。 . 。
