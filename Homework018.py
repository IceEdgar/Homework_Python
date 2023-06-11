from random import randint
n = int(input('Введите количество элементов в списке: '))
some_list = []
for i in range(n):
    some_list.append(randint(0, 10))
print(some_list)
min_number = int(input('Введите минимальный диапазон (от 0 до 10) - '))
max_number = int(input('Введите максимальный диапазон (от 0 до 10) - '))
for i in range(len(some_list)):
    if min_number <= some_list[i] <= max_number:
        print(f'индекс элемента {i} ===> {some_list[i]}')