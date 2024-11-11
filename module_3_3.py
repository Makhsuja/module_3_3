def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [111, False, 'Green']
values_dict = {"a": 121, "b": 'String', "c": False}
values_list_2 = ['Food', 5.45]
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
