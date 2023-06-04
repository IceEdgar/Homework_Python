def rev(n):
    if n == 0:
        return ""
    k = input("Введите число: ")
    return rev(n-1)+(k)+(' ')


n = int(input("Введите количество элементов: "))
print(rev(n))
