# Переменная итератор используется внутри цикла.

# for i in 'hello':
#     print(i)

# for j in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
#     print(j ** 2)

# range()
# for number in range(1, 11):  # 1, 2, 3, 4...
#     print(number)
#
# for number in range(5):
#     print(number)
#
# for number in range(2, 101, 2):
#     print(number, end=' ')

# for number in range(10, 1, -2):
#     print(number)


# Переменная итератор не используется внутри цикла.
# 100 раз вывести слово hello в консоль

# i = 1
# while i <= 100:
#     print('Hello')
#     i += 1

# for _ in range(100):  # 0, 1, 2, 3, 4, 5, 6, 7, 8...99
#     print('Hello')

# # Вводится количество чисел, затем сами числа, если число = 10, вывести YES и закончить ввод,
# # в конце вывести NO если никакое из чисел не было равно 10.
# n = int(input('Введите кол-во чисел: '))
# for _ in range(n):
#     number = int(input())
#     if number == 10:
#         print('YES')
#         break
# else:
#     print('NO')