# Homework. Task 4_3.
# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.
#
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
#
# in
# -1
# out
# Negative value of the number of numbers!
# []
#
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random
import os
clear = lambda: os.system('cls')
clear()

def get_random_list(len_list: int):
    rnd_list = random.choices(range(2 * len_list), k=len_list)
    return rnd_list

def get_unique_items(input_list: list):
    output_list = []
    for i in range(len(input_list) - 1):
        if input_list.count(input_list[i]) == 1:
            output_list.append(input_list[i])
    return output_list


value = input('Enter a positive integer: ')
if value.isdigit() and int(value) > 0:
    random_list = get_random_list(int(value))
    result = get_unique_items(random_list)
    print(f'{random_list}\n{result}')
else:
    print('Error. Incorrect input.')