# Homework. Task 5_3.
# Создайте программу для игры в "Крестики-нолики".
# Поле 3x3. Игрок - игрок, без бота.

import os
clear = lambda: os.system('cls')
clear()

def playfield(data_tab):
    print("+---+---+---+")
    for i in range(3):
        print("|", data_tab[0 + i * 3],\
              "|", data_tab[1 + i * 3],\
              "|", data_tab[2 + i * 3], "|",)
        print("+---+---+---+")

def who_won(data_steps):
    winner_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],\
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],\
                    [0, 4, 8], [2, 4, 6]]
    for j in winner_lines:
        if data_steps[j[0]] == data_steps[j[1]] == data_steps[j[2]]:
            return data_steps[j[0]]
    return False

def is_valid_step(value, data_tab):
    return 1 <= value <= 9 and data_tab[value - 1] != "X" and data_tab[value - 1] != "O"


tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The game started")
game_on = True
player = 1
step_counter = 0

while game_on == True:
    playfield(tab)
    valid = True

    while valid == True and game_on == True:
        if player == 1 and step_counter < 9:
            pos = int(input("Player 1,\nselect a position X (enter a number from 1 to 9): "))
            step = "X"
            if is_valid_step(pos, tab):
                tab[pos - 1] = step
                playfield(tab)
                valid = True
                step_counter += 1
                player = 2
            else:
                print("Incorrect input")
                valid = False
        elif player == 2 and step_counter < 9:
            pos = int(input("Player 2,\nselect a position O (enter a number from 1 to 9): "))
            step = "O"
            if is_valid_step(pos, tab):
                tab[pos - 1] = step
                playfield(tab)
                valid = True
                step_counter += 1
                player = 1
            else:
                print("Incorrect input")
                valid = False

        if who_won(tab) == False:
            continue
        elif step_counter >= 9:
            game_on = False
            winner = "N"
            break
        else:
            game_on = False
            winner = who_won(tab)
            break

print("The game finished.")
if winner == "X":
    print("Player 1 won.")
elif winner == "O":
    print("Player 2 won.")
else:
    print("Drawn game.")






