def pos(number):
    if number == 0:
        return ""
    x=input("Введите число: ")
    return pos(number-1)+(x)+(' ')

number = int(input("Введите количество элементов: "))
print(pos(number))