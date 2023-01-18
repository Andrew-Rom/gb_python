# Homework. Task 6_1.
# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

import random

q_ty = input('Enter the number of elements in the list (2<): ')
if q_ty.isdigit() and int(q_ty) > 2:
    q_ty = int(q_ty)
    random_list = [random.randint(1,100) for i in range(q_ty)]
    print(random_list)
    res_list = [random_list[i] for i in range(1, q_ty) if random_list[i] > random_list[i - 1]]
    print(res_list)
else:
    print('Incorrect input')