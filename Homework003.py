'''Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?'''

Sum = int(input("Введите общее количество журавликов: "))
if Sum<6:
     print(f'Сделал какой-то другой ученик {Sum} журавлика')
elif Sum % 6==0:
     x = Sum // 6
     print(f'Катя сделала {x * 4} журавлика')
     print(f'Сережа сделал {x} журавлика')
     print(f'Петя сделал {x} журавлика')
else:
     x = Sum // 6
     print(f'Катя сделала {x * 4} журавлика')
     print(f'Сережа сделал {x} журавлика')
     print(f'Петя сделал {x} журавлика')
     print(f'Сделал какой-то другой ученик {Sum - x*6} журавлика')