# Homework. Task 6_2.
# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

first_item = 20
last_item = input(f'Enter the last item of list (greater or equal to {first_item}): ')
if last_item.isdigit() and int(last_item) >= first_item:
    last_item = int(last_item)
    res_list = [i for i in range(first_item, last_item + 1)\
                if i % first_item == 0 or i % (first_item +1) == 0]
    print(res_list)
else:
    print('Incorrect input')