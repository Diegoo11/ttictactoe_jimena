import random

TABLE = [[[" "], [" "], [" "]], [[" "], [" "], [" "]], [[" "], [" "], [" "]]]


def view_table():
    first_row = "| "
    for column in TABLE[0]:
        first_row += column[0] + " | "  # x | O | X |

    second_row = "| "
    for column in TABLE[1]:
        second_row += column[0] + " | "

    tridh_row = "| "
    for column in TABLE[2]:
        tridh_row += column[0] + " | "

    print(first_row)
    print(second_row)
    print(tridh_row)
    print("---------------------------")


def view_winner(player):
    if all([TABLE[0][0] == player, TABLE[0][1] == player, TABLE[0][2] == player]):
        return True
    elif all([TABLE[1][0] == player, TABLE[1][1] == player, TABLE[1][2] == player]):
        return True
    elif all([TABLE[2][0] == player, TABLE[2][1] == player, TABLE[2][2] == player]):
        return True
    elif all([TABLE[0][0] == player, TABLE[1][0] == player, TABLE[2][0] == player]):
        return True
    elif all([TABLE[0][1] == player, TABLE[1][1] == player, TABLE[2][1] == player]):
        return True
    elif all([TABLE[0][2] == player, TABLE[1][2] == player, TABLE[2][2] == player]):
        return True
    elif all([TABLE[0][0] == player, TABLE[1][1] == player, TABLE[2][2] == player]):
        return True
    elif all([TABLE[2][0] == player, TABLE[1][1] == player, TABLE[0][2] == player]):
        return True
    else:
        return False


ENDGAME = False

print("COMENZO EL JUEGO")

SHIFT = random.randint(0, 1)
# 0 == jugador X
# 1 == jugador O


while not ENDGAME:
    JUGADOR = ""
    if SHIFT == 0:
        print("Le toca al jugador X")
        JUGADOR = "x"
    else:
        print("Le toca al jugador O")
        JUGADOR = "o"
    view_table()
    print("Haz tu jugada en x")
    played_x = int(input())  # input ingresa un dato pero en String
    print("Haz tu jugada en Y")
    played_y = int(input())

    TABLE[played_y][played_x] = JUGADOR

    if SHIFT == 0:
        SHIFT = 1
    else:
        SHIFT = 0
    if view_winner(JUGADOR):
        print("GANADORRRRRR")
        ENDGAME = True



print("Game Over")
