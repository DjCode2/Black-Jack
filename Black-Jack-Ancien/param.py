import tkinter as tk
from tkinter import ttk
import fonction

# Définir la fonction obtenir_valeurs
def obtenir_valeurs(entree_nb_joueurs, entree_mise):
    global nb_joueurs  
    global mise 
    nb_joueurs = int(entree_nb_joueurs.get())
    mise = int(entree_mise.get())
    return nb_joueurs, mise

def jouer (entree_nb_joueurs,entree_mise,root_param):
    obtenir_valeurs(entree_nb_joueurs, entree_mise)
    fonction.BouclePrincipale(root_param)


# Définir la fonction paramètre

def paramètre(root_menu):
    global nb_joueurs 
    global mise
    root_menu.destroy()
    root_param = tk.Tk()
    root_param.title("Choix des joueurs et de la mise")
    root_param.geometry("500x200")

    # Style
    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 18))

    fenetre = tk.Frame(root_param, padx=20, pady=10)
    fenetre.pack(expand=True, fill='both', anchor='center')

    # Entrée pour choisir le nombre de joueurs
    label_nb_joueurs = ttk.Label(fenetre, text="Nombre de joueurs souhaité (entre 1 et 7):")
    label_nb_joueurs.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entree_nb_joueurs = ttk.Entry(fenetre)
    entree_nb_joueurs.grid(row=0, column=1, padx=10, pady=5)

    # Entrée pour choisir la mise
    label_mise = ttk.Label(fenetre, text="Mise (en euros) :")
    label_mise.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entree_mise = ttk.Entry(fenetre)
    entree_mise.grid(row=1, column=1, padx=10, pady=5)

    # Bouton jouer
    bouton_jouer = ttk.Button(fenetre, text="Jouer", command=lambda: jouer(entree_nb_joueurs,entree_mise,root_param))
    bouton_jouer.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

    root_param.mainloop()
