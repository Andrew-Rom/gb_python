# Homework. Task 6_3.
# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

#"Иван","Мария","Петр","Илья","Марина","Петр","Алина","Бибочка"

def create_dict(input_data):
    input_data = sorted((input_data).replace('"','').split(','))
    keys_list = sorted(set([input_data[i][:1] for i in range(len(input_data))]))
    output_dict = {key: [] for key in keys_list}
    for i in range(len(input_data)):
        for key in output_dict.keys():
            if key == input_data[i][:1]: output_dict[key].append(input_data[i])
    return output_dict

value = input('Enter names of employees: ')
result = create_dict(value)
print(result)