def print_params():
    a = 1
    b = 'строка'
    c = True
    print (a, b, c)
print_params()


def print_params():
    a = 1
    b = 'строка'
    c = True
    print (a, c)
print_params()


def print_params():
    a = 1
    b = 'строка'
    c = True
    print ()
print_params()


def print_params():
    a = 1
    b = 'строка'
    c = True
    print ()
print_params(b = 25)


def print_params():
    a = 1
    b = 'строка'
    c = True
    print ()
print_params(c = [1,2,3])


values_list = ['cat', b, 3]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}


def print_params(a, b, c):
    print(a, b, c)

values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)

values_list = ['cat', True, 3]
print(*values_list)


def print_params(a, b, c):
    print(a, b, c)
values_list_2 = ['friend', 25]
print_params(*values_list_2, 42)