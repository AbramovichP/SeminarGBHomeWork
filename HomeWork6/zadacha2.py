"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

Диапазон от 6 до 12

Вывод: [1, 9, 13, 14, 19]
"""
from random import randint


def random_list():#заполняет первый список рандомными значениями и возвращает его
    list_1 = []
    n = int(input("Введите сколько элементов будет в списке: "))
    for _ in range(n):
        list_1.append(randint(-10,10))
    return list_1

def diapason():#Создает диапазон из введенных значений возвращая списком
    list_2 = []
    diapason_min = int(input("Введите первый элемент диапазона: "))
    diapason_max = int(input("Введите последний элемент диапазона: "))
    if diapason_min > diapason_max:
         for i in range(diapason_min,diapason_max-1,-1):
             list_2.append(i)
    for j in range(diapason_min,diapason_max+1):
        list_2.append(j)
    return list_2

def search_elem(list_1,list_2):# ищет совпадения значений элементов двух списков и записывает индексы первого списка в третий возвраща его
    list_3 = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                list_3.append(i)
    return list_3
    
list_1 = random_list()
print('Дан рандомно созданный список: \n',list_1)

diapason_list = diapason()
print('Заданный диапазон:\n',*diapason_list)

print(f'Индексы элементов списка, значения которых принадлежат заданному диапазону:\n{search_elem(list_1,diapason_list)}')