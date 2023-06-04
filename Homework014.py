def Chek(number):
    for i in range(2, number):
        if number % i == 0:
            return (f"Число {number} не простое")

        return (f"Число {number} простое")


number = int(input("Ввeдите число: "))
print(Chek(number))