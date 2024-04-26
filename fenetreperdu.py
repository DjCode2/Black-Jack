# projet black jack
"""Clément, Théo, Maïwenn"""

import tkinter as tk
import tkinter as tk
import subprocess #eviter import circulaire

import param 

def creer_fenetre_perdu(root, resultat):
    # Fonction appelée lorsque le bouton est cliqué
    def Rejouer(root):
        root.destroy()
        fenetre.destroy()
        subprocess.call(["python", "mainloop.py"]) #eviter les imports circulaires

    def quitter(root):
        root.destroy()
        fenetre.destroy()


        
        

    # Créer la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("resultat")

    fenetre.geometry("450x320")

    # Étiquette avec le message "Vous avez perdu"
    etiquette = tk.Label(fenetre, text=f"Vous avez {resultat}", font=("Arial", 18))
    etiquette.pack(pady=10)

    # Étiquette avec le message de la mise
    mise_label = tk.Label(fenetre, text=f"Votre mise était de {param.mise}", font=("Arial", 12))
    mise_label.pack(pady=15)

    # Bouton "Quitter"
    rejouer_btn = tk.Button(fenetre, text="Rejouer", width=14, font=("Arial", 25), bg="green", command=lambda: Rejouer(root))
    rejouer_btn.pack()

    bouton_quitter = tk.Button(fenetre, text="Quitter", width=14, font=("Arial", 25), bg="red", command=lambda: quitter(root))
    bouton_quitter.pack()




    # Boucle principale de la fenêtre
    fenetre.mainloop()