"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
from random import randint


n = int(input('Введите кол-во элементов в массиве: '))

def create_array(n): # создает массив с рандомными числами от 1 до 10
    array = []
    for _ in range(n):
        array.append(randint(1, 10))

    return array

a = create_array(n)
print(a)

x = int(input("Введите число: "))

def search_num(array, x): # ищет ближайшее по значению число в массиве
    
    search = x + 1
    search2 = x - 1

    for i in array:
        if i == x:
            return i
    for i in range(x):
        for j in array:
            if j == search:
                return j
            elif j == search2:
                return j
        search += 1
        search2 -= 1  
    
result = search_num(a,x)
print(f'Cамый близкий по величине элемент к заданному числу {x} в данном массиве равен: {result}')