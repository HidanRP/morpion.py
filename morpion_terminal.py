# création de grille et affichage
grille = [" " for i in range(9)]

def afficher_grille():
    print("  ---------")
    print("  " + grille[0] + " | " + grille[1] + " | " + grille[2])
    print("  ---------")
    print("  " + grille[3] + " | " + grille[4] + " | " + grille[5])
    print("  ---------")
    print("  " + grille[6] + " | " + grille[7] + " | " + grille[8])
    print("  ---------")

#fonction de tour a jouer
def tour(grille, joueur):
    while True:
        colonne = int(input("Entrez le numéro de la colonne : "))
        ligne = int(input("Entrez le numéro de la ligne : "))
        if grille[colonne + ligne * 3] == " ":
            grille[colonne + ligne * 3] = "X" if joueur == 1 else "O"
            afficher_grille()
            break
        else:
            print("Cette case est déjà jouée ! Saisissez une autre case svp !")
#fonction du gagnant
def est_gagnant(grille):
    for i in range(3):
        if grille[i*3] == grille[i*3+1] == grille[i*3+2] and grille[i*3] != " ":
            return 1
    for i in range(3):
        if grille[i] == grille[i+3] == grille[i+6] and grille[i] != " ":
            return 1
    if grille[0] == grille[4] == grille[8] and grille[0] != " ":
        return 1
    if grille[2] == grille[4] == grille[6] and grille[2] != " ":
        return 1
    return 0
#fonction en cas de match nul
def est_match_nul(grille):
    for i in range(9):
        if grille[i] == " ":
            return 0
    return 1
#joueurs
joueur = 1
print("Le joueur 1 possède les X. Le joueur 2 possède les O")
afficher_grille()
gagne = 0
while gagne == 0:
    tour(grille, joueur)
    if est_gagnant(grille):
        print("Le joueur " + str(joueur) + " remporte la partie")
        gagne = 1
    elif est_match_nul(grille):
        print("Plus de place ! Match nul !")
        gagne = 1
    else:
        joueur = 2 if joueur == 1 else 1