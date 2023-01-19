# Homework. Task 6_4.
# Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь,
# ключи — первые буквы фамилий,
# значения — словари, реализованные по схеме предыдущего задания.

#"Иван Сергеев","Инна Серова","Петр Алексеев","Илья Иванов","Анна Савельева","Юнона Ветрякова","Борис Аркадьев","Антон Серов","Павел Анисимов"

def create_dict(input_data):
    input_data = input_data.replace('"','').split(',')
    temp1 = [input_data[a].split() for a in range(len(input_data))]
    keys_list_surname = set([temp1[ks][1][:1] for ks in range(len(temp1))])
    dict_surnames = {key_s: {} for key_s in keys_list_surname}

    for key_s in dict_surnames.keys():
        temp2 = []
        for i in range(len(input_data)):
            if key_s == temp1[i][1][:1]:
                temp2.append(input_data[i])
                keys_list_name = sorted(set([temp2[kn][0][:1] for kn in range(len(temp2))]))
                dict_names = {key_n: [] for key_n in keys_list_name}
                for j in range(len(temp2)):
                    for key_n in dict_names.keys():
                        if key_n == temp2[j][0][:1]: dict_names[key_n].append(temp2[j])
                dict_surnames[key_s] =dict(dict_names)
    return dict_surnames

value = input('Enter first and last names of employees (in the format «Name Surname»): ')
result = create_dict(value)
print(result)
