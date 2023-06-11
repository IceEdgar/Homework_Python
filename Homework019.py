song = input('Введите песенку Винни Пуха: ')
letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
song_list = song.split()
rithm = list()
for i in song_list:
    count = 0
    for j in i:
        if j in letters:
            count = count+1
    rithm.append(count)
res = all(x == rithm[0] for x in rithm)
if res:
    print('Парам пам-пам')
else:
    print('Пам парам')
