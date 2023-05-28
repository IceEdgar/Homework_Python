# Вводятся строки, пока не будет введена пустая строка. Если длина очередного введеного слова равна 5, то
# нужно вывести сообщение "YES" и прекратить возможность ввода для пользователя, если таких слов нет, то
# вывести 'NO' один раз в конце.

flag = True
while True:
    some_str = input()
    # if some_str == '':
    #     break
    if not some_str:
        break
    if len(some_str) == 5:
        print('YES')
        flag = False
        break
if flag:
    print('NO')

'''some_str = input()
while some_str:
    if len(some_str) == 5:
        print('YES')
        break
    some_str = input()
else:
    print('NO')'''