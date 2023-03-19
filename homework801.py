"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной """

def import_fail ():
    import importlib
    username = str(input("Введите название файла с расширением: "))
    contact = open(username)
    for line in contact:
        print(line, end = '')
    return contact
 
def menu():
    print("0. Импорт файла")
    print("1. Добавить новый контакт")
    print("2. Поиск контакта")
    print("3. Просмотр всех контактов")
    print("4. Выход")

    choice = int(input("Сделайте свой выбор: "))
    return choice

def add_contact():
    x = []
    for i in range(len(x[0])):
        if i == 0:
            x.append(input("Введите фамилию: "))
        if i == 1:
            x.append(input("Введите имя: "))
        if i == 3:
            x.append(input("Введите отчество: "))
        if i == 4:
            x.append(input("Введите номер: "))
    x.append(x)
    return x

def search_contact():
    choice = int(input("\n 1. Фамилия\n 2. Имя\n 3. Отчество\n 4. Номер\n\
                 \n Выберите критерий поиска: "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Введите фамилию:"))
    for i in range(len(contact[0])):
        if query == contact[i][0]:
            check = i
            temp.append(contact[i])
    if choice == 2:
        query = str(input("Введите имя:"))
    for i in range(len(contact[0])):
        if query == contact[i][1]:
            check = i
            temp.append(contact[i])
    if choice == 3:
        query = str(input("Введите отчество:"))
    for i in range(len(contact)):
            if query == contact[i][2]:
                check = i
                temp.append(contact[i])
    if choice == 4:
        query = str(input("Введите номер:"))
    for i in range(len(contact)):
            if query == contact[i][3]:
                check = i
                temp.append(contact[i])
    else:
        print("Ошибка")
        return -1
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check

def display_all():
    if not contact:
        print("Контактов нет!")
    else:
        for i in range(len(contact)):
            print(contact[i])

im = import_fail()
choice = menu()
if choice == 1:
    contact = add_contact(x)
elif choice == 2:
    d = search_contact()
    if d == -1:
        print("The contact does not exist. Please try again")
else:
    choice == 3
    display_all()