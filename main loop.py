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
largeur_fenetre = 1230
hauteur_fenetre = 762
root.resizable(False, False)

photo = tk.PhotoImage(file="BlackjackMenu.png")
image_label = tk.Label(root, image=photo)
image_label.pack()

root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}") #définir la taille de la fenetre indépendament du contenu

#def les boutons
jouer_button = tk.Button(root, text="Jouer",font=("Arial", 25), width=10, command=ouvrir_fenetre_jeu)
quitter_button = tk.Button(root, text="Quitter", width=10, font=("Arial", 25), bg="red" , command=quitter_jeu)

#placer le titre et les boutons 

jouer_button.place(x=520,y=450)
quitter_button.place(x=520, y=520)


# Lancer la boucle principale
root.mainloop()

