"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
from random import randint

x = randint(1, 1000)
y = randint(1, 1000)
s = x + y
p = x * y
print("Петя задумывает два натуральных числа.\nПомогите Кате отгадать задуманные Петей числа.")
print(f"Подсказки:\nСумма двух задуманных чисел равна:{s}")
print(f"Произведение этих чисел равно: {p}")


one = int(input("Попробуем отгадать!\n Введите число: "))

while one != x and one != y and one != 0:
    one = int(input("Пока не верно, введите число или 0 если сдаётесь: \n"))
if one == 0:
    print(f"Вы сдались! А числа были равны: {x} и {y}")
elif one == x:
    print("Да! Одно число отгадано! Вы молодец! Попробуем отгадать второе: ")
    two = int(input("Введите число: "))
    while two != y and two != 0:
        two = int(input("Пока не верно, введите число или 0 если сдаётесь: \n"))
    if two == 0:
        print(f"Вы сдались! А числа были равны: {x} и {y}")
    else:
        print(f"Да! Победа! Вы помогли Кате отгадать. Загаданные числа были: {x}, {y}")    
else:
    print("Да! Одно число отгадано! Вы молодец! Попробуем отгадать второе: ")
    two = int(input("Введите число: "))
    while two != x and two != 0:
        two = int(input("Пока не верно, введите число или 0 если сдаётесь: \n"))
    if two == 0:
        print(f"Вы сдались! А числа были равны: {x} и {y}")
    else:
        print(f"Да! Победа! Вы помогли Кате отгадать. Загаданные числа были: {x}, {y}")
