# Homework. Task 3_2.
# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

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

sum_of_pair_list = []
for i in range(len_of_list // 2):
    temp = rnd_list[i] + rnd_list[len_of_list - 1 - i]
    sum_of_pair_list.append(temp)
if len_of_list % 2 != 0:
    sum_of_pair_list.append(rnd_list[len_of_list // 2])
print(sum_of_pair_list)