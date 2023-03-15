"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import randint
    
n = int(input("Введите кол-во монеток:\n")) # число монеток
coins = []
reshka = 0
orel = 0

for _ in range(n): # кидаем монетки :)
    coins.append(randint(0,1))

for i in range(n):
    if coins[i] == 0:
        reshka += 1
    elif coins[i] == 1:
        orel += 1

print(coins)
print(reshka,orel)

if reshka <= orel:
    print("{} - монет нужно перевернуть.".format(reshka))

else:
    print("{} - монет нужно перевернуть.".format(orel))

