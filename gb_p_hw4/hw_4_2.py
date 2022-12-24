# Homework. Task 4_2.
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# in
# 54
# out
# [2, 3, 3, 3]
#
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
#
# in
# 650
# out
# [2, 5, 5, 13]

import os
clear = lambda: os.system('cls')
clear()

def get_simple_multipliers (number: int):
    result = []
    multiplier = 2
    while multiplier * multiplier <= number:
        if number % multiplier == 0:
            result.append(multiplier)
            number = number // multiplier
        else:
            multiplier += 1
    if number > 1:
        result.append(number)
    return result

value = input('Enter a positive integer: ')
if value.isdigit() and int(value) > 0:
    print(get_simple_multipliers(int(value)))
else:
    print('Error. Incorrect input.')
