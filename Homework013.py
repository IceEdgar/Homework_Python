word = ""
some_list = input('Введите текст - ')+' '
print(some_list)
set_word =set()
for i in range(len(some_list)):
    if some_list[i] not in " ,.:;":
        word = word + some_list[i]
    else:
        set_word.add(word)
        word = ""
print('Количество одинаковых слов в строке', set_word, '=',len(set_word))
