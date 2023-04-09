"""
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
__________________________________________________
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
"""
def menu():
    """Меню справочника"""
    menu_choice = 0

    while (menu_choice != '1' and menu_choice != '2'
            and menu_choice != '3' and menu_choice != '4'):
        print('-' * 120)
        print("Телефонный справочник:\n 1 - Просмотр контактов;\n 2 - Сохранение нового контакта;\n 3 - Поиск контакта (Изменение и Удаление);\n 4 - Выход \n Ввод: ")
        menu_choice = input()

    return menu_choice

def writing_file(file):
    """Запись в список контакта"""
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    patronymic = input('Отчество: ')
    phone_number = input('Номер телефона: ')
    file.write(f'{last_name} {first_name} {patronymic} {phone_number}\n')
    return file

def search_file(list_file):
    """Поиск контакта в файле"""
    print('-' * 120)
    last_name = input('Введите одну из характеристик для поиска определенной записи(Например имя или фамилию человека):\n')
    new_list = []
    for i in list_file:
        if last_name in i:
            new_list.append(i)
    return new_list

def submenu(one_list, two_list):
    submenu_choise = 0
    while (submenu_choise != '1' and submenu_choise != '2' and submenu_choise != '3'):
        print('Дальнейшие действия: \n 1 - Удаление найденого контакта \n 2 - Изменение контакта \n 3 - Возврат в основное меню\n Ввод:')
        submenu_choise = input()
    if submenu_choise == '1':
        one_list.remove(two_list[0])
    elif submenu_choise == '2':
        one_list.remove(two_list[0])
        first_name = input('Имя: ')
        last_name = input('Фамилия: ')
        patronymic = input('Отчество: ')
        phone_number = input('Номер телефона: ')
        one_list.append(f'{last_name} {first_name} {patronymic} {phone_number}')
    return one_list

def main():
    user_selection = 0
    
    while user_selection != '4':
        user_selection = menu()

        if user_selection == '1':
            file = open('phonebook.txt', encoding='utf-8') 
            print('-' * 120)
            print(file.read())
            file.close()

        elif user_selection == '2':
            file = open('phonebook.txt','a')
            writing_file(file)
            file.close()
    
        elif user_selection == '3':
            file = open('phonebook.txt')
            file_list = file.read().split('\n')[:-1]
            file.close
            # print(file_list)
            n = search_file(file_list)
            if n == []:
                print('Ничего не найдено')
            else:
                print(n)
                finish_list = submenu(file_list, n)
                file = open('phonebook.txt', 'w')
                for i in finish_list:
                    file.write(i + '\n')
                file.close           
    print('Выход выполнен.')
            
if __name__ == "__main__":
    main()