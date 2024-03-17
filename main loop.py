#sécu des imports
import os
while True:
    try:
        import tkinter as tk
        print("l'import c'est bien passé")
        break #on sort si les instal se sont bien passé
    except ImportError:
        print("erreur d'import, une des bibliothèques n'est pas sur la machine ou n'est pas reconnue")
        break

#def des fct
def ouvrir_fenetre_jeu():
    pass

def quitter_jeu():
    root.quit()

# crée le menu
root = tk.Tk()
root.title("Menu")

# def la fenetre 
largeur_fenetre = 300
hauteur_fenetre = 200
root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}") #définir la taille de la fenetre indépendament du contenu

# placer le titre et les boutons
Titre = tk.Label(root, text="Bienvenue dans notre jeu", font=("Yu Mincho", 16))
jouer_button = tk.Button(root, text="Jouer",font=("Arial", 12), width=10, command=ouvrir_fenetre_jeu)
quitter_button = tk.Button(root, text="Quitter", width=10, font=("Arial", 12), bg="red", command=quitter_jeu)
text_blague = tk.Label(root, text="Please don't do that, dont quit :'(", font=("Arial", 8), fg="gray")


#placer le titre et les boutons avec .pack, il les place automatiquement au milieu
Titre.pack(pady=20)
jouer_button.pack(pady=10)
quitter_button.pack(pady=10)
text_blague.pack()

# Lancer la boucle principale
root.mainloop()
