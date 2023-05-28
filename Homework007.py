a = int(input('Задай сумму двух чисел '))
b = int(input('Задай произведение чисел '))
c = 0
for i in range(a + b):
    if c:
        break
    for j in range(a + b):
        if i + j == a and i * j == b:
            c = 1
            print(f'первое число ={i}, второе число ={j}')
            break