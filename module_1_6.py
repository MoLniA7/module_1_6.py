my_dict = {'Vlad' : 2005, 'Max' : 2000, 'Andrey' : 1997}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Denis', 'Такого имени нет'))
my_dict.update({'Pasha' : 2003, 'Mia' : 2010})
save = my_dict.pop('Max')
print(save)
print(my_dict)
print(' ')
my_set = {3, 5, 8, 5, 'car', 8, 'cat', 5, 'car'}
print(my_set)
my_set.update({4, 'aplle'})
my_set.remove(5)
print(my_set)
