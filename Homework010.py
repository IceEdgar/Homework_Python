from random import randint
n = int(input('Введите количество элементов: '))
x = int(input('Введите число, для проверки: '))
list = []
for i in range(n):
    list.append(randint(0, 10))
print(list)
min = abs(x - list[0])
index = 0
for i in range(1, n):
    count = abs(x - list[i])
    if count < min:
        min = count
        index = i
print(f'Число {list[index]} в списке A наиболее близко по величине к числу {x}')