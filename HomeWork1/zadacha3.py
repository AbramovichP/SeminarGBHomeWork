"""
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
 Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""
ticket = int(input("Введите 6-ти значный номер билета: "))

while ticket < 100000 or ticket > 999999:
    print("Введен не 6-ти значный номер!")
    ticket = int(input("Введите 6-ти значный номер билета: "))

def SumOfDigits(x): # Сумма цифр в числе
    result = 0
    while x != 0:
        result += x % 10
        x //= 10  
    return result

theFirstHalf = ticket // 1000
theSecondHalf = ticket % 1000
resultFirstHalf = SumOfDigits(theFirstHalf)
resultSecondHalf = SumOfDigits(theSecondHalf)

if resultSecondHalf == resultFirstHalf:
    print("{} --> YES".format(ticket))
else:
    print("{} --> NO".format(ticket))