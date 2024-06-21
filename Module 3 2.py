
print('Функция с параметрами по умолчанию:')

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print('Распаковка параметров:')

def print_params(alpha, beta, gamma):
    print(alpha, beta, gamma)

values_list = [12, 'Лисица', True]
values_dict = {'alpha': 9, 'beta': 'Hirsch', 'gamma': True}

print_params(*values_list)
print_params(**values_dict)

print('Распаковка + отдельные параметры:')

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print('(print_params(*values_list_2, 42)) работает. Список распаковался.')


