#Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.
#Площадь круга

#r = int(input('Введите радиус круга: '))

#print((r*r)*3.14)

#Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.

#num = int(input('Ввидите число - '))
#if (num >= 1000 and num <= 9999) or (num <= -1000 and num >= -9999):
#    print('YES')
#else:
#    print('NO')


n = int(input('Введите целое число: ')) 
 
if n > 0: 
    if n % 2 == 0: 
        print('положительное четное число') 
    else: 
        print('положительное нечетное число') 
elif n == 0: 
    print('ноль') 
else: 
    if n % 2 == 0: 
        print('отрицательное четное число') 
    else: 
        print('отрицательное нечетное число')