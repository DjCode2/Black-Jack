import tkinter as tk

def choisir_valeur(valeur,root):
    choix_as = valeur
    root.destroy()
    
    

def afficher_interface_choix_as():
    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Choix de valeur")

    # Label pour afficher le message
    message_label = tk.Label(fenetre, text="Vous avez un As, choisissez 1 ou 11")
    message_label.pack(pady=10)

    # Bouton pour choisir 1
    bouton_1 = tk.Button(fenetre, text="1", width=10, command=lambda: choisir_valeur(1))
    bouton_1.pack(pady=5)

    # Bouton pour choisir 11
    bouton_11 = tk.Button(fenetre, text="11", width=10, command=lambda: choisir_valeur(11))
    bouton_11.pack(pady=5)

    # Lancement de la boucle principale
    fenetre.mainloop()

# Appeler la fonction pour afficher l'interface
afficher_interface_choix_as()