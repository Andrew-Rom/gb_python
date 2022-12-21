# Homework. Task 3_3.
# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
#
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011

import os
clear = lambda: os.system('cls')
clear()

value = input('Введите десятичное число: ')
if value.isdigit() and value != '0':
    num10 = int(value)
else:
    print('Введены некорректные данные.')
    exit()

num2 = 0
counter = 0
while num10 > 0:
    temp = num10 % 2
    num2 = temp * (10 ** counter) + num2
    num10 = int(num10 / 2)
    counter += 1
print('Результат перевода в двоичную систем счисления: ', num2)