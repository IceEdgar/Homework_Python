'''В некоторой школе решили набрать три новых математических 
класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.'''

desk1 = int(input('Введите количесво учащихся '))
desk2 = int(input('Введите количесво учащихся '))
desk3 = int(input('Введите количесво учащихся '))

a = (desk1//2 + desk1 %2)
b = (desk2//2 + desk2 %2)
c = (desk3//2 + desk3 %2)
print ('' a + b + c)