mult = 1
number = int(input())
while number != 0:
    if number % 10 == 4:
        mult *= number
    number = int(input())
if mult == 1:
    mult = 0
print(mult)