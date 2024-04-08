# projet black jack
"""Clément, Théo, Maïwenn"""

while True:
    try:
        import tkinter as tk
        import random
        print("l'import c'est bien passé")
        break #on sort si les instal se sont bien passé
    except ImportError:
        print("erreur d'import, une des bibliothèques n'est pas sur la machine ou n'est pas reconnue")
        break



#tapis = tk.Tk()

# generation du paquet de carte 
def jeu_de_carte ():
    carte=[]
    symboles=["trèfle","coeur","carreau","pique"]
    valeurs=["as","valet","dame","roi","2","3","4","5","6","7","8","9","10"]
    for symbole in symboles:
        for valeur in valeurs:
            if valeur=="valet" or valeur=="dame" or valeur=="roi":
                cartes=(symbole,valeur,10)
            elif valeur=="as":
                cartes=(symbole,valeur,1)
            else :
                cartes=(symbole,valeur,int(valeur))
            carte.append(cartes)
    return carte

def debut ():
    joueur_debut=1
    return joueur_debut

def changement_joueur(player): # pour le multijoueur a faire a la fin
    #nombre_de_joueur=int(input("combien de joueur?"))
    #assert nombre_de_joueur<5 and nombre_de_joueur>0
    # numpy array et implementer avec le nombre de joueur donner 
    #ou for de nombre de joueur et crer une list
    if player==1: #joueur
        player=2 #croupier
    else :
        player=1
    return player

# fonction determiner la carte distribué + actualisation du jeu de carte 
def carte_a_distribuer(jeucarte):
    nombre=random.randint(0,len(jeucarte)-1)
    carte_donner=jeucarte[nombre] #on donne la carte 
    if carte_donner[1]=="as": # dans le cas ou on a un as
        valeur_as=int(input("1 ou 11"))
        assert valeur_as==1 or valeur_as==11
        carte_donner2=(carte_donner[0],carte_donner[1],valeur_as)
        carte_donner=carte_donner2
    jeucarte.pop(nombre)
    return (carte_donner,jeucarte)

#fonction determiner les carte d'une main et le score 
def main_joueur(carte,joueur,mainj,mainc,scorej,scorec):
    if joueur==1:
        mainj.append(carte)
        scorej+=carte[2]
    else:
        mainc.append(carte)
        scorec+=carte[2]

    joueur=changement_joueur(joueur)
    print(joueur)
    return(mainc,scorec,joueur,mainj,scorej)

def action_joueur(scrore_joueur,jeu,joueur,mainjoueur):
    if scrore_joueur<21:
        carte_sup=input("saisissez 'carte' si vous souahiter une carte en plus")
        assert carte_sup=="carte"
        carte_supplementaire=int(input("saisissez le nombre de carte en plus"))
        for i in range (carte_supplementaire):
            cartesup=carte_a_distribuer(jeu)
            score_final=main_joueur(cartesup,joueur,mainjoueur,None,scrore_joueur,None)
    return score_final        

def fin_de_jeu(scorejoueur,scorecroupier,main_joueur):
    if scorejoueur<21 and scorejoueur<scorecroupier:
        return ("perdu")
    elif scorejoueur==21 and len(main_joueur)==2:
        return ("black jack")
    elif scorejoueur==scorecroupier or scorejoueur==21 and scorejoueur==scorecroupier :
        return ("egalité")
    else :
        return ("gagner")

# programme principale / sera plus tard dans un autre dossier
#tapis.mainloop()
