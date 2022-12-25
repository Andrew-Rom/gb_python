# Homework. Task 4_4.
# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
#
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
#
# in
# 0
# -1
# 4
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

import random
import os
clear = lambda: os.system('cls')
clear()

degree = input('Enter degree of the polynomial: ')

if degree.isdigit() and int(degree) >= 1:
    degree = int(degree)
    coefficients = random.sample(range(0, 10), k=degree)
    polynomial = ''
    for i in range(len(coefficients)):
        if i != len(coefficients) - 1 \
                and i != len(coefficients) - 2 \
                and coefficients[i] != 0:
            polynomial += f'{coefficients[i]}*x^{len(coefficients) - i - 1}'
            if coefficients[i + 1] != 0:
                polynomial += ' + '
        elif i == len(coefficients) - 2 \
                and coefficients[i] != 0:
            polynomial += f'{coefficients[i]} * x'
            if coefficients[i + 1] != 0:
                polynomial += ' + '
        elif i == len(coefficients) - 1 \
                and coefficients[i] != 0:
            polynomial += f'{coefficients[i]} = 0'
        elif i == len(coefficients) - 1 \
                and coefficients[i] == 0:
            polynomial += ' = 0'
    with open('file_task_hw_4_4.txt', "a", encoding="utf-8") as out_file:
        out_file.write(f'{polynomial}\n')
else:
    print('Error. Incorrect input.')
