def print_params(a=1, b='строка', c=True):
   print(a, b, c)


print_params()
print_params(b=25)
c = [1, 2, 3]
print_params(*c)

values_list = ['b', False, 2]
values_dict = {'a': 'one', 'b': 1, 'c': 1.1}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
