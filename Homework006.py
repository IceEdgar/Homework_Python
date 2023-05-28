n = int(input('КВведите кол-во монеток: '))
list = []
count1=0
count2=0
from random import randint
 
for i in range(n):
    list.append(randint(0,1))
    if list[i]==0:
        count1+=1
    else:
        count2+=1
print(list,'0-Решка, 1-Орел')
if count1<count2:
    print('Минимальное число монеток, которые нужно перевернуть -', count1)
else:
    print('Минимальное число монеток, которые нужно перевернуть -', count2)