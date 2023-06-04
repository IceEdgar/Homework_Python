from random import randint
n = int(input('Введите количество элементов в первом множестве: '))
m = int(input('Введите количество элементов во втором множестве:  '))
some_list1 = []
some_list2 = []
some_set = {}
for i in range(n):
    some_list1.append(randint(0, 10))
print(some_list1)
for i in range(m):
    some_list2.append(randint(0, 10))
print(some_list2)
some_set = set(sorted(some_list1+some_list2))
print(some_set)