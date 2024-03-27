#fonction.py
import tkinter as tk

def quitter_menu(root_menu):
    root_menu.quit()

def ouvrir_fenetre_jeu(root_menu):
    # Fermer la fenêtre de menu
    root_menu.destroy()
    # Ouvrir la fenêtre de jeu principal
    root_jeu = tk.Tk()
    root_jeu.title("BlackJack")
    # Ajoutez ici le contenu de votre fenêtre de jeu principal
    root_jeu.mainloop()