from HWView import *


def write_name(name):
    with open("tel.txt","a") as file:
        file.write(name)

def read_found(a):
    with open("tel.txt","r") as file:
        lst = file.readlines()
        for i in lst:
            if a in i:
                print(i)
    

def sorting(type_sorting):
    with open("tel.txt","r") as file:
        lst = file.readlines()
        lst.sort(key = lambda x: int(x.split(",")[type_sorting-1]))
    with open("tel.txt","w") as file:
        for i in range(len(lst)):
            file.write(lst[i])

def delete_row(delete):
    with open("tel.txt","r") as file:
        lst = file.readlines()
        for i in range(len(lst)):
            if delete in lst[i]:
                print(lst[i],"\n","Для удаления строки введите - 1")
                res = int(input())
                if res == 1:
                    lst.pop(i)
                    break
    with open("tel.txt","w") as file:
        for i in range(len(lst)):
            file.write(lst[i])

def changing(changing_row):
    with open("tel.txt","r") as file:
        lst = file.readlines()
        for i in range(len(lst)):
            if changing_row in lst[i]:
                lst[i] = input_name()
    with open("tel.txt","w") as file:
        for i in range(len(lst)):
            file.write(lst[i])

