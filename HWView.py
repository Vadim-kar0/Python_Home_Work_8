def input_num():
    ask = int(input("Выбери действие:\n1 - Записать нового пользователя\n2 - поиск по характеристике\n3 - сортировка списка \n4 - удаление строки\n5 - изменение строки \n0 - выход из программы\n"))
    return ask

def input_name():
    name = input("Введите индекс: \n") +', '+ input("Введите имя: \n") +', '+ input("Введите номер: \n")+"\n"
    return name
 

def input_found():
    found = input("Введите параметр для поиска: \n")
    return found

def input_sorting():
    type_sorting = int(input("Введите параметр для сортировки:\n1 - по индексу \n2 - по имени \n3 - по номеру\n"))
    return type_sorting

def input_delete():
    changing_row = input("Введите часть данных строки для её удаления: \n")
    return changing_row


def input_changing():
    changing_row = input("Введите часть данных строки для её изменения: \n")
    return changing_row

