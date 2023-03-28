"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 

"""
def exponentiation(a,b):#Рекурсия, возведение в степень числа
    if b == 0:
        return 1
    elif b < 0:
        return exponentiation(a,b+1) * 1/a
    return exponentiation(a,b-1) * a
 
a = int(input('Введите число: '))
b = int(input('Введите в какую степень возвести число: '))

print(f'Число {a} в степени {b} равно: {exponentiation(a,b)}')