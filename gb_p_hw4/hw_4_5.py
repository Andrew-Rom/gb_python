# Homework. Task 4_5.
# 5. Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!

import os
import copy
clear = lambda: os.system('cls')
clear()

# Получение данных из файла
def get_list_from_file(my_file):
    data_list = []
    file = open(my_file)
    for line in file:
        data_list.append(''.join(line.replace(' = 0\n', '')))
    file.close()
    return data_list

# Создание списка одночленов из многочлена
def get_list_of_monomials(value):
    monomials_list = []
    for i in range(len(value)):
        monomials_list.append(value[i].split(' + '))
    return monomials_list

# Создание списка коэффициент-степень
def get_coefficients_and_degrees(value):
    for i in range(len(value)):
        for j in range(len(value[i])):
            if '*x^' in value[i][j]:
                coefficient = int(value[i][j][:value[i][j].find('*')])
                degree = int(value[i][j][(value[i][j].find('^') + 1):])
                value[i][j] = [coefficient, degree]
            elif ('*x' in value[i][j]) and (not '^' in value[i][j]):
                coefficient = int(value[i][j][:value[i][j].find('*')])
                degree = 1
                value[i][j] = [coefficient, degree]
            elif not 'x' in value[i][j]:
                coefficient = int(value[i][j])
                degree = 0
                value[i][j] = [coefficient, degree]
    return value

file1 = get_list_from_file('file_task_hw_4_4.txt')
file2 = get_list_from_file('file_task_hw_4_4ad.txt')
monomials1 = get_list_of_monomials(file1)
monomials2 = get_list_of_monomials(file2)
monomials1_c_d = get_coefficients_and_degrees(monomials1)
monomials2_c_d = get_coefficients_and_degrees(monomials2)

# Суммирование коэффициентов в соответствии со степенью
result = []
if len(monomials1) != len(monomials2):
    print('The contents of the files do not match!')
for i in range(len(monomials1_c_d)):
    if len(monomials1_c_d[i]) > len(monomials2_c_d[i]):
        result.append(monomials1_c_d[i].copy())
        for j in range(len(monomials2_c_d[i])):
            for jj in range(len(monomials1_c_d[i])):
                if monomials2_c_d[i][j][1] == monomials1_c_d[i][jj][1] and monomials2_c_d[i][j][1] != 0:
                    result[i][jj][0] = result[i][jj][0] + monomials2_c_d[i][j][0]
                elif monomials2_c_d[i][j][1] == 0 and monomials1_c_d[i][jj][1] == 0:
                    result[i][jj][0] = result[i][jj][0] + monomials2_c_d[i][j][0]
            if monomials2_c_d[i][j][1] == 0 and monomials1_c_d[i][j][1] != 0:
                result[i].append(monomials2_c_d[i][j].copy())
    else:
        result.append(monomials2_c_d[i].copy())
        for j in range(len(monomials1_c_d[i])):
            for jj in range(len(monomials2_c_d[i])):
                if monomials1_c_d[i][j][1] == monomials2_c_d[i][jj][1] and monomials1_c_d[i][j][1] != 0:
                    result[i][jj][0] = result[i][jj][0] + monomials1_c_d[i][j][0]
                elif monomials1_c_d[i][j][1] == 0 and monomials2_c_d[i][jj][1] == 0:
                    result[i][jj][0] = result[i][jj][0] + monomials1_c_d[i][j][0]
            if monomials1_c_d[i][j][1] == 0 and monomials2_c_d[i][-1][1] != 0:
                result[i].append(monomials1_c_d[i][j].copy())

# Формирование строки с многочленом, полученым в результате суммирования, и выгрузка в файл
for a1 in range(len(result)):
    output_line = ''
    for a2 in range(len(result[a1])):
        output_line += f'{result[a1][a2][0]}*x^{result[a1][a2][1]} + '
    output_line = output_line.replace('1*', '').replace('x^1', 'x').replace('*x^0', '')[:-3] + ' = 0'
    with open('file_task_hw_4_5.txt', "a", encoding="utf-8") as out_file:
        out_file.write(f'{output_line}\n')
