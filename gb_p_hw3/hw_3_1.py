# Homework. Task 3_1.
# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22

import random
import os
clear = lambda: os.system('cls')
clear()

value = input('Введите количество элементов генерируемого списка: ')
if value.isdigit() and value != '0':
    len_of_list = int(value)
else:
    print('Введены некорректные данные.')
    exit()

rnd_list = random.sample(range((len_of_list + 1) * 2), len_of_list)
print(rnd_list)

sum_of_odd_pos_items = 0
for i in range(0, len_of_list, 2):
    sum_of_odd_pos_items += rnd_list[i]
print('Cуммa элементов списка, стоящих на нечётных позициях: ', sum_of_odd_pos_items)