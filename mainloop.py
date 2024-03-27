# main.py

while True:
    try:
        import os
        import tkinter as tk
        import fonction
        print("l'import c'est bien passé")
        break #on sort si les instal se sont bien passé
    except ImportError:
        print("erreur d'import, une des bibliothèques n'est pas sur la machine ou n'est pas reconnue")
        break

# crée le menu
root_menu = tk.Tk()
root_menu.title("Menu")

largeur_fenetre_menu = 1230
hauteur_fenetre_menu = 762
root_menu.resizable(False, False)
#gérer le fond
photo = tk.PhotoImage(file="BlackjackMenu.png")
image_label = tk.Label(root_menu, image=photo)
image_label.pack()
root_menu.geometry(f"{largeur_fenetre_menu}x{hauteur_fenetre_menu}") #définir la taille de la fenetre indépendament du contenu

#def les boutons du menu
jouer_button = tk.Button(root_menu, text="Jouer",font=("Arial", 25), width=10, command=lambda: fonction.ouvrir_fenetre_jeu(root_menu))
quitter_button = tk.Button(root_menu, text="Quitter", width=10, font=("Arial", 25), bg="red" , command=lambda: fonction.quitter_menu(root_menu))

#placer le titre et les boutons du menu
jouer_button.place(x=520,y=450)
quitter_button.place(x=520, y=520)














# Lancer la boucle principale
root_menu.mainloop()