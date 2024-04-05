import tkinter as tk
import fonction

# Crée le menu
def creer_menu():
    root_menu = tk.Tk()
    root_menu.title("Menu")

    largeur_fenetre_menu = 1230
    hauteur_fenetre_menu = 762
    root_menu.resizable(False, False)

    # Charger l'image de fond
    photo = tk.PhotoImage(file="BlackjackMenu.png")
    image_label = tk.Label(root_menu, image=photo)
    image_label.pack()

    # Définir la taille de la fenêtre indépendamment du contenu

    # Définir les boutons du menu
    jouer_button = tk.Button(root_menu, text="Jouer", font=("Arial", 25), width=10, command=lambda: fonction.ouvrir_fenetre_jeu(root_menu))
    quitter_button = tk.Button(root_menu, text="Quitter", width=10, font=("Arial", 25), bg="red", command=root_menu.quit)

    # Placement du titre et des boutons du menu
    jouer_button.place(x=520, y=450)
    quitter_button.place(x=520, y=520)

    # Lancer la boucle principale
    root_menu.mainloop()


creer_menu()