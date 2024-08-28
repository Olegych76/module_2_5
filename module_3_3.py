def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# интерпретатор сразу предупреждает, что это недопустимые параметры, поэтому закомментировал:
# b должен быть типом str
# print_params(b = 25)
# с должен быть bool
# print_params(c=[1, 2, 3])

values_list = [25, True, "string"]
# распаковываем список с другими типами данных на место трёх параметров нашей функции:
print_params(*values_list)

# создаём словарь; в качестве значений, вместо int берём bool, вместо строки - список, вместо bool - float
values_dict = {'a': False,
               'b': ['element1', 'element2'],
               'c': 1.25}
# распаковываем словарь с несоответствующими значениями ключей в нашу функцию:
print_params(**values_dict)

# создаём укороченный список (без одного параметра):
values_list2 = [3.14, False]
# параметры функции переопределяются новыми типами, недостающий параметр берёт значение по умолчанию:
print_params(*values_list2)
