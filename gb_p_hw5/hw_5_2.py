# Homework. Task 5_2.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
clear = lambda: os.system('cls')
clear()

def encode_file_into_new_file(input_file, output_file):
    file = open(input_file)
    data_list = []
    for line in file:
        data_list.append(line.replace('\n', ''))
    file.close()
    rle_output = []
    for i in range(len(data_list)):
        output = ''
        temp = list(data_list[i])
        item = temp.pop(0)
        counter = 1
        for j in temp:
            if j == item:
                counter += 1
            else:
                output += (str(counter) + item)
                item = j
                counter = 1
        output += (str(counter) + item)
        rle_output.append(output)
    with open(output_file, "a", encoding="utf-8") as out_file:
        out_file.write('\n'.join(rle_output))

def decode_file_and_output(encoded_file):
    file = open(encoded_file)
    data_list = []
    for line in file:
        data_list.append(line.replace('\n', ''))
    file.close()
    output_list = []
    for i in range(len(data_list)):
        output = ''
        temp = list(data_list[i])
        count = ''
        for j in temp:
            if j.isdigit():
                count += j
            else:
                output += (j * int(count))
                count = ''
        output_list.append(output)
    return output_list

file_input = input("Enter the name of the file with the text: ")
file_encode = input("Enter the file name to record: ")
file_decode = input("Enter the name of the file to decode: ")
encode_file_into_new_file(file_input, file_encode)
result = decode_file_and_output(file_decode)
print('\n'.join(result))