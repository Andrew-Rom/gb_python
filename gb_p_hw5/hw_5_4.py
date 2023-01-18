# Homework. Task 5_3.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота, можно не добвлять.
# 2. Подумайте, как наделить бота "интеллектом".

import random

import os
clear = lambda: os.system('cls')
clear()

def bot(total_candies, limit):
    step = total_candies % limit + 1
    if not step:
        step = randint(1, limit + 1)
    return step

candies_total = 2021
candies_limit = 28

game_type = None
while not game_type in range(1,3):
    game_type = int(input("Choose game:\n\t"
                          "1. Human (player 1) vs. Human (player 2)\n\t"
                          "2. Human (player 1) vs. Bot (player 2)\n"
                          "Enter '1' or '2': "))
print(f"The game started.\nYou can take any amount of candy but not more than {candies_limit}.")

player = random.randint(1, 2)
print(f"First: player {player}")

while candies_total > 0:
    print(f"\nNow amount of candy is: {candies_total}.")
    if game_type == 2 and player == 2:
        player_step = bot(candies_total, candies_limit)
        print(f"The bot took {player_step} candies")
        player = 1
    elif game_type == 2 and player == 1:
        player_step = int(input(f"Player {player}, take: "))
        if player_step <= 0 or player_step > candies_limit:
            print("Incorrect input")
        else:
            candies_total -= player_step
            player = 2
    elif game_type == 1 and player == 1:
        player_step = int(input(f"Player {player}, take: "))
        if player_step < 0 or player_step > candies_limit:
            print("Incorrect input")
        else:
            candies_total -= player_step
            player = 2
    elif game_type == 1 and player == 2:
        player_step = int(input(f"Player {player}, take: "))
        if player_step < 0 or player_step > candies_limit:
            print("Incorrect input")
        else:
            candies_total -= player_step
            player = 1

print("The game finished.")
if game_type == 2 and player == 2:
    print("The bot won and took all candies.")
else:
    print(f"The player {player} won and took all candies.")