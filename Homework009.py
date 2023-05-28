n = int(input('Введите количество элементов: '))
x = int(input('Введите число, для проверки: '))
list = []
count=0
from random import randint
 
for i in range(n):
    list.append(randint(0,10))
    if list[i]==x:
        count+=1
print(list)
print(f'Число {x} встречается {count} раз.')