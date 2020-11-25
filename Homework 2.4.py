my_list = input('Введите несколько слов через пробел: ')
for int, word in enumerate(my_list.split(' '), 1):
    print(int, word[:10])
