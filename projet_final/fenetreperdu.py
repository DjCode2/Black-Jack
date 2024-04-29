# projet black jack
"""Clément, Théo, Maïwenn"""

import tkinter as tk
import tkinter as tk
import subprocess #eviter import circulaire
import param 

def creer_fenetre_perdu(root, resultat):

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

    fenetre.geometry("450x320")

    # Étiquette avec le message "Vous avez perdu"
    if param.nb_joueurs >=1:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 1 à  {resultattest[0]}", font=("Arial", 18))
        etiquette1.pack(pady=10)
    
    if param.nb_joueurs >=2:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 2 à  {resultattest[1]}", font=("Arial", 18))
        etiquette1.pack(pady=10)

    if param.nb_joueurs >=3:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 3 à  {resultattest[2]}", font=("Arial", 18))
        etiquette1.pack(pady=10)

    if param.nb_joueurs >=4:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 4 à  {resultattest[3]}", font=("Arial", 18))
        etiquette1.pack(pady=10)

    if param.nb_joueurs >=5:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 5 à  {resultattest[4]}", font=("Arial", 18))
        etiquette1.pack(pady=10)

    if param.nb_joueurs >=6:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 6 à  {resultattest[5]}", font=("Arial", 18))
        etiquette1.pack(pady=10)

    if param.nb_joueurs >=7:
        etiquette1 = tk.Label(fenetre, text=f"le joueur 7 à  {resultattest[6]}", font=("Arial", 18))
        etiquette1.pack(pady=10)




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


