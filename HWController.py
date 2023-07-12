from HWDatabase import *
from HWView import *

def main():
    while True:
        num = input_num()
        if num == 0:
            break
        if num == 1:
            name = input_name()
            write_name(name)
            print("Успешно записано\n")
        if num == 2:
            a = input_found()
            print(read_found(a))
        if num == 3:
            type_sorting = input_sorting()
            sorting(type_sorting)
            print("Файл отсортирован\n")
        if num == 4:
            delete = input_delete()
            delete_row(delete)
            print("Строка удалена\n")

        if num == 5:
            changing_row = input_changing()
            changing(changing_row)
            print()
        


            

main()

