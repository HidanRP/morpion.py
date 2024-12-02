import tkinter

def check_nul():
    # Si personne n'a gagné, déclarer un match nul
    global win
    if not win:
        count = 0
        for row in range(3):
            for col in range(3):
                if buttons[row][col]['text'] in ['X', 'O']:
                    count += 1
        if count == 9:
            print("Match nul :/")
            win = True

def print_winner():
    # Affiche le joueur gagnant
    global win
    win = True
    print("Le joueur", current_player, "a gagné !")

def switch_player():
    # Change le joueur courant
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def check_win(clicked_row, clicked_col):
    global win
    if win:
        return

    # Détecter la victoire de façon horizontale
    if all(buttons[clicked_row][i]['text'] == current_player for i in range(3)):
        print_winner()
        return

    # Détecter la victoire de façon verticale
    if all(buttons[i][clicked_col]['text'] == current_player for i in range(3)):
        print_winner()
        return

    # Détecter la victoire en diagonale (haut gauche -> bas droite)
    if all(buttons[i][i]['text'] == current_player for i in range(3)):
        print_winner()
        return

    # Détecter la victoire en diagonale (haut droite -> bas gauche)
    if all(buttons[i][2 - i]['text'] == current_player for i in range(3)):
        print_winner()
        return

    # Vérifier si le match est nul
    check_nul()

def place_symbol(row, column):
    # Place le symbole du joueur si la case est vide
    clicked_button = buttons[row][column]
    if not win and clicked_button['text'] == "":
        clicked_button.config(text=current_player)
        check_win(row, column)
        if not win:
            switch_player()

def draw_grid():
    # Dessine la grille de jeu
    for row in range(3):
        buttons_row = []
        for col in range(3):
            button = tkinter.Button(
                root, font=('Arial', 100),
                width=4, height=1,
                command=lambda r=row, c=col: place_symbol(r, c)
            )
            button.grid(row=row, column=col)
            buttons_row.append(button)
        buttons.append(buttons_row)

# Stockage
buttons = []
current_player = 'X'
win = False

# Faire la fenêtre du jeu
root = tkinter.Tk()

# Personnalisation de la fenêtre
root.title("TicTacToe")
root.minsize(500, 500)

draw_grid()
root.mainloop()
