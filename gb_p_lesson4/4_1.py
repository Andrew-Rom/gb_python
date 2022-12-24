# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.



def check ():
    enter_list = input("Введите числа через пробел").split()
    right_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("!,;")
        if enter_list[i].isdigit:
            right_list.append(enter_list[i])
    print(right_list)
    return right_list


def max_min_finder(any_list):
    if any_list:
        return max(any_list, key=int), min(any_list, key=int)
    return []

print(*max_min_finder(check()))