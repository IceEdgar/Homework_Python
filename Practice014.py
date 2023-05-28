n = int(input('КВведите кол-во элементов: '))
list1 = []
for _ in range(n):
     list1.append(int(input()))
second = []
for i in list1:
    if i not in second:
        second.append(i)
print(len(second))