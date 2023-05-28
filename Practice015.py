

nums = int(input("Введите кол-во элементов: "))
some_list = []
for _ in range(nums):
    some_list.append(int(input()))
print("Исходная последовательность: ", some_list)

K = int(input("Введите количество элементов для сдвига: "))
K = K % nums  # делаем сдвиг циклическим
some_list = some_list[-K:] + some_list[:-K]  # сдвигаем последовательность

print("Последовательность, сдвинутая на", K, "элементов: ", some_list)
Artem  кому  Все 23:23
n = int(input('КВведите кол-во элементов: '))
some_list = []
for _ in range(n):
     some_list.append(int(input()))

print(some_list)
count=0
for i in range(0, len(some_list)-1):
    if some_list[i] != some_list[i + 1]:
         count += 1

print(count)

nums = int(input("Введите кол-во элементов: "))
some_list = []
for _ in range(nums):
    some_list.append(int(input()))
print("Исходный список: ", some_list)
count=0

for i in range(0, len(some_list)-1):
    if some_list[i] < some_list[i + 1]:
         count += 1

print(count)