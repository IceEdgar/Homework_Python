
def print_phonebook():
    with open('phonebook.txt','r') as p:
        print(p.read())

def add_information():
    with open('phonebook.txt','a') as p:
        p.write('\n')
        p.write(input('Введите ФИО и номер: '))

def search():
    with open('phonebook.txt','r') as p:
        a = input('Введите искомый номер или ФИО: ')
        for line in p:
            if a in line.casefold(): print(line)

while True:
    p = input("Введите цыфру из МЕНЮ:\n1 - Просмотр всего справочника\n2 - Введите номер или ФИО для поиска\n3 - Добавить запись в справочник\n")
    if  p == '1': print_phonebook() 
    elif p == '2': search()
    elif p == '3': add_information()
    else:
        print('Некорректный ввод')
    print()     