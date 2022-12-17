# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
#
#  1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

import os
clear = lambda: os.system('cls')
clear()

value = input('Введите натуральное число N: ')
if not (value.isdigit()):
    print('Введены некорректные данные.')
else:
    n = int(value)
    result = []
    for i in range(1, n + 1):
        item = i
        temp = 1
        while item > 1:
            temp *= item
            item -= 1
        result.append(temp)
    print(result)