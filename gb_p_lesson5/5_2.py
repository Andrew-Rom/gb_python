# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.

from random import choices

def any_list(num):
    return choices(range(1, num+2), k=num)

def seq(some_list):
    temp_list = []
    for i in range(len(some_list)):
        num_1 = some_list[i]
        out_list = [num_1]
        for j in range(i+1, len(some_list)):
            if some_list[j] > num_1:
                num_1 = some_list[j]
                out_list.append(num_1)
        if len(out_list) > 1:
            temp_list.append(out_list)
    return temp_list

a = any_list(10)
print(a)
print(seq(a))