"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
n = int(input("Введите число: "))
result = 0
k = 0

while result <= n:
    result = 2**k
    k += 1
    if result <= n:
        print(result, end=' ')
print()