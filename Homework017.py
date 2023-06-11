def arithmetic_progression(a, d, n):
    for i in range(n):
        print(a + i * d)

a = int(input('Введите первый элемент массива - '))
d = int(input('Введите разность элементов массива - '))
n = int(input('Введите количество элементов массива - '))
arithmetic_progression(a, d, n)
