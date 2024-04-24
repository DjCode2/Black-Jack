import tkinter as tk
import fonction

# Définir la fonction obtenir_valeurs
def obtenir_valeurs(entree_nb_joueurs, entree_mise):
    global nb_joueurs  
    global mise 
    nb_joueurs = int(entree_nb_joueurs.get())
    mise = int(entree_mise.get())
    return nb_joueurs, mise

# Définir la fonction paramètre
def paramètre(root_menu):
    global nb_joueurs 
    global mise
    root_menu.destroy()
    root_param = tk.Tk()
    root_param.title("Choix des joueurs et de la mise")

    fenetre = tk.Frame(root_param)
    fenetre.pack(padx=40, pady=10)

    # Entrée pour choisir le nombre de joueurs
    label_nb_joueurs = tk.Label(fenetre, text="Nombre de joueurs souhaité (entre 2 et 3):")
    label_nb_joueurs.grid(row=0, column=0, padx=10, pady=5)
    entree_nb_joueurs = tk.Entry(fenetre)
    entree_nb_joueurs.grid(row=0, column=1, padx=10, pady=5)

    # Entrée pour choisir la mise
    label_mise = tk.Label(fenetre, text="Mise (en euros) :")
    label_mise.grid(row=1, column=0, padx=10, pady=5)
    entree_mise = tk.Entry(fenetre)
    entree_mise.grid(row=1, column=1, padx=10, pady=5)

    # Bouton valider
    bouton_valider = tk.Button(fenetre, text="Valider", command=lambda : obtenir_valeurs(entree_nb_joueurs, entree_mise))
    bouton_valider.grid(row=2, columnspan=2, padx=10, pady=10)

    # Bouton jouer
    bouton_jouer = tk.Button(fenetre, text="Jouer", command=lambda : fonction.BouclePrincipale(root_param))
    bouton_jouer.grid(row=3, columnspan=2, padx=10, pady=10)

    root_param.mainloop()
