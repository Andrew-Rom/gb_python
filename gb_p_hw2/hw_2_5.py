# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
#
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
import os
clear = lambda: os.system('cls')
clear()

n = int(input('Enter the quantity of items: '))
first_list = list(range(n))
second_list = first_list[:]
for i in range(len(second_list)):
    random_index = random.randint(0, (len(second_list) - 1))
    temp = second_list[i]
    second_list[i] = second_list[random_index]
    second_list[random_index] = temp
print(first_list)
print(second_list)