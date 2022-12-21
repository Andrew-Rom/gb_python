# Homework. Task 3_4.
# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

import random
from decimal import Decimal
import os
clear = lambda: os.system('cls')
clear()

def get_random_float_list(value, round_value=2):
    new_list = []
    for i in range(value):
        temp = round(random.uniform(1, 10), round_value)
        new_list.append(temp)
    return new_list

value = input('Введите количество элементов генерируемого списка: ')
if value.isdigit() and value != '0':
    len_of_list = int(value)
else:
    print('Введены некорректные данные.')
    exit()

rnd_list = get_random_float_list(len_of_list)
print(rnd_list)

for i in range(len_of_list):
    temp = Decimal(str(rnd_list[i])) - int(rnd_list[i])
    rnd_list[i] = float(temp)
rnd_list = sorted(rnd_list)
print('Min:', rnd_list[0], end=', ')
print('Max:', rnd_list[-1], end='. ')
print('Difference:', Decimal(str(rnd_list[-1])) - Decimal(str(rnd_list[0])))