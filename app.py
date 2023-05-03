import random

TABLE = [
        [[" "], [" "], [" "]],
        [[" "], [" "], [" "]],
        [[" "], [" "], [" "]]
]


def view_table():
    first_row = "| "
    for column in TABLE[0]:
        first_row += column[0] + " | "  # x | O | X |

    second_row = "| "
    for column in TABLE[1]:
        second_row += column[0] + " | "

    tridh_row = "| "
    for column in TABLE[1]:
        tridh_row += column[0] + " | "

    print(first_row)
    print(second_row)
    print(tridh_row)
    print("---------------------------")


ENDGAME = False

print("COMENZO EL JUEGO")

SHIFT = random.randint(0, 1)
# 0 == jugador X
# 1 == jugador O


while not ENDGAME:
    if SHIFT == 0:
        print("Le toca al jugador X")
    else:
        print("Le toca al jugador O")
    view_table()
    input()

    # SI AHORA LE TOCA AL JUGADOR 0 ESTONCES QUE DESPUES LE TOQUE AL JUGADOR X, Y BISEVERSA


print("Game Over")
