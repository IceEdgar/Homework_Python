'''Задача 4. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза'''


watermelons = int(input('Введите кол-во арбузов: '))

max_kg = int(input('Введите массу арбуза: '))
min_kg = max_kg
for _ in range(watermelons - 1):
    weight = int(input('Введите массу арбуза: '))
    if weight > max_kg:
        max_kg = weight
    else:
        if weight < min_kg:
            min_kg = weight
print(f'Для себя любимого - {max_kg}, для любимой тещи - {min_kg}')