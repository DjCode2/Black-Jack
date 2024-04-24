import tkinter as tk
import fonction

def obtenir_valeurs(curseur_mise,curseur_joueurs,root_param):
    nb_joueurs = int(curseur_joueurs.get())
    mise = curseur_mise.get()

    nb_joueur_lst=[]
    for i in range(1, nb_joueurs+1):
        nb_joueur_lst.append(i) #liste allant de 1 au nombre de joueur, pour après pouvoir faire
        #5 systèmes de cartes et les lancer que si leur numéro est dans la liste
    
    print("Mise sélectionnée (en euros) :", mise)
    print("liste de joueur", nb_joueur_lst)

    fonction.BouclePrincipale(root_param)





def paramètre(root_menu):
    root_menu.destroy()
    root_param = tk.Tk()
    root_param.title("Choix des joueurs et de la mise")

    # Cadre principal + titre 
    fenetre = tk.Frame(root_param)
    label_param = tk.Label(root_param, text="Paramètre : ",font=("Arial", 16))
    label_param.pack(padx=40, pady=20)
    fenetre.pack(padx=40, pady=10)

    # Curseur Snombre de joueurs
    label_joueur = tk.Label(fenetre, text="Nombre de joueurs souhaité:")
    label_joueur.grid(row=0, column=0, padx=10, pady=5)
    curseur_joueurs = tk.Scale(fenetre, from_=1, to=5, orient=tk.HORIZONTAL, length=200)
    curseur_joueurs.grid(row=0, column=1, padx=10, pady=5)

    # Curseur mise
    label_mise = tk.Label(fenetre, text="Mise (en euros) :")
    label_mise.grid(row=1, column=0, padx=10, pady=5)
    curseur_mise = tk.Scale(fenetre, from_=1, to=100, orient=tk.HORIZONTAL, length=200)
    curseur_mise.grid(row=1, column=1, padx=10, pady=5)

    # Bouton valider
    bouton_valider = tk.Button(fenetre, text="Valider", command=lambda : fonction.BouclePrincipale(root_param))
    bouton_valider.grid(row=2, columnspan=2, padx=10, pady=10)

    root_param.mainloop()
