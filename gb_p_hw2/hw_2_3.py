#3. Задайте список из n чисел,
# заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
#
# in
# 6
#
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

import os
clear = lambda: os.system('cls')
clear()

value = input('Введите натуральное число N: ')
if not (value.isdigit()):
    print('Введены некорректные данные.')
else:
    output_list = []
    n = int(value)
    sum = 0
    for i in range(1, n + 1):
        item = round(((1 + 1 / i) ** i), 3)
        output_list.append(item)
        sum += item
    print(output_list)
    print(sum)