"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""
def nums_sum(a,b):
    if b == 0:
        return a
    return nums_sum(a+1,b-1)
       
a = int(input("Введите целое не отрицательное число: "))
b = int(input("Введите целое не отрицательное число: "))

print(f'Сумма этих чисел равна: {nums_sum(a,b)}')