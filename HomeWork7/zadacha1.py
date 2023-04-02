"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
**Вывод:** Парам пам-пам 
"""

def split_a_phrase (phrase):
    """Разбивает строку на список строк"""
    List_vini = phrase.split(' ')
    return List_vini

def counting_vowels (vini_list):
    """Подсчитывает кол-во гласных в списке"""    
    vowels = 0
    vowels_list = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
    for i in vowels_list:
        for j in vini_list:
            for elm in j:
                if i == elm:
                    vowels += 1 
    return vowels

def main():
    phrase = input()
    vini_list = split_a_phrase(phrase)
    if counting_vowels(vini_list) % len(vini_list) == 0:
        print('Парам пам-пам')
    else:
        print('Пам парам')

if __name__=="__main__":
    main()