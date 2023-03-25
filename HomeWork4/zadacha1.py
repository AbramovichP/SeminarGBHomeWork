"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
def create_set(a,s): #Создает множество заполняемое от руки
    list_1 = set()
    
    for _ in range(a+1):
        list_1.add(int(input(s)))
    return list_1

def sort_set(my_set):#Создает из множества список, сортирует в порядке возрастания
    my_list = list(my_set)
    temp = 0
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))

my_set_1 = create_set(n,'Введите элемент первого множества: ')
print()
my_set_2 = create_set(m,'Введите элемент втрого множества: ')
print('Элементы первого множества: \n', my_set_1)
print('Элементы второго множества: \n', my_set_2)
my_set_3 = my_set_1.intersection(my_set_2)

sor_list = sort_set(my_set_3)
print('В обоих множествах встречаются: ', *sor_list)