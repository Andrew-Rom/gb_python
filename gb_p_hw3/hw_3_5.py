# Homework. Task 3_5.
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

import os
clear = lambda: os.system('cls')
clear()

value = input('Введите число: ')
if value.isdigit() and value != '0':
    value = int(value)
else:
    print('Введены некорректные данные.')
    exit()

fib_list = [0, 1]
neg_fib_list = []
for i in range(1, value + 1):
    fib_list.append(fib_list[-1] + fib_list[-2])
    neg_fib_list.insert(0, (-1) ** (i + 1) * fib_list[i])
neg_fib_list.extend(fib_list[:-1])
print(*neg_fib_list)