# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
#
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

from decimal import Decimal
import os
clear = lambda: os.system('cls')
clear()

value = input('Введите число для поиска суммы суммы его цифр: ')
if not (value.replace('-', '').replace('.', '').isdigit()):
    print('Введены некорректные данные.')
else:
    number = float(value)
    integer_part_of_num = int(abs(number))
    temp_number = Decimal(value)
    fractional_part_of_num = abs(temp_number) - integer_part_of_num
    sum_of_integers = 0
    sum_of_fractions = 0
    while integer_part_of_num > 0:
        sum_of_integers += int(integer_part_of_num % 10)
        integer_part_of_num /= 10
    while fractional_part_of_num > 0:
        temp = int((fractional_part_of_num * 10)) % 10
        sum_of_fractions += temp
        fractional_part_of_num = fractional_part_of_num * 10 - temp
    result = sum_of_integers + sum_of_fractions
    print('Сумма цифр данного числа: ', result)

