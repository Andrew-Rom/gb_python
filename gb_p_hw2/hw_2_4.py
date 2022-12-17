# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

import os
clear = lambda: os.system('cls')
clear()

n = int(input('Enter the value of N: '))
pos1 = int(input('Position one: '))
pos2 = int(input('Position two: '))
output = list(range((n * (-1)), 0))
temp = list(range(n + 1))
output = output + temp
print(output)
if (pos1 > 0 and pos1 <= len(output)) and (pos2 > 0 and pos2 <= len(output)):
    result = output[pos1 - 1] * output[pos2 - 1]
    print(result)
else:
    print('There are no values for these indexes!')