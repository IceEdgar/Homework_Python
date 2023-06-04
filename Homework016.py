def rev(n):
    if n == 0:
        return print('')
    k = int(input('Введите число: '))
    rev(n - 1)
    return print(k)


n = int(input('Введите количество элементов: '))
rev(n)
