"""
projekt_2b.py: Druhý projekt do Engeto Online Python Akademie

author: Jan Koppan
email: jan.koppan@seznam.cz
"""
# Funkce pro vytištění úvodního textu a pravidel hry
def print_intro():
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("========================================")
    print("Let's start the game")

# Funkce pro zobrazení hracího pole
def print_board(board):
    print("--------------------------------------------")
    print("+---+---+---+")
    for i in range(0, 9, 3):  # Procházení pole po řádcích
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("+---+---+---+")
    print("============================================")

# Funkce pro kontrolu platnosti tahu
def is_valid_move(board, move):
    # Zkontrolujeme, jestli je vstup číslo a jestli je pozice volná
    return move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " "

# Funkce pro kontrolu výhry
def check_win(board, player):
    # Možné kombinace pro výhru (horizontálně, vertikálně, diagonálně)
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # řádky
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # sloupce
        [0, 4, 8], [2, 4, 6]              # diagonály
    ]
    for line in wins:
        if all(board[i] == player for i in line):  # Zkontrolujeme, jestli jsou všechny pozice stejné
            return True
    return False

# Funkce pro kontrolu remízy
def is_draw(board):
    # Pokud není žádná volná pozice, je remíza
    return all(cell != " " for cell in board)

# Hlavní funkce pro hraní hry
def play_game():
    board = [" " for _ in range(9)]  # Vytvoření prázdného hracího pole
    current_player = "o"  # Začíná hráč 'o'

    print_intro()  # Vytisknutí úvodního textu
    print_board(board)  # Vytisknutí hracího pole

    while True:
        print(f"Player {current_player} | Please enter your move number: ", end="")
        move = input().strip()

        if not move.isdigit():  # Kontrola, jestli vstup je číslo
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        move = int(move)  # Převedení vstupu na číslo
        if move < 1 or move > 9:  # Kontrola, jestli je číslo v povoleném rozsahu
            print("Number out of range! Please enter a number between 1 and 9.")
            continue

        if board[move - 1] != " ":  # Kontrola, jestli je pozice volná
            print("That position is already taken! Choose another one.")
            continue

        board[move - 1] = current_player  # Umístění tahu na hrací pole
        print_board(board)  # Vytisknutí aktualizovaného hracího pole

        if check_win(board, current_player):  # Kontrola, jestli někdo vyhrál
            print(f"Congratulations, the player {current_player} WON!")
            break

        if is_draw(board):  # Kontrola, jestli je remíza
            print("It's a draw! Well played both.")
            break

        # Přepnutí na druhého hráče
        current_player = "x" if current_player == "o" else "o"

# Spuštění hry
if __name__ == "__main__":
    play_game()