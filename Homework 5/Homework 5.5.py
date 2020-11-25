num = input('Введите числа разделенные пробелом: ').split(' ')
with open('text5.txt', 'w+', encoding='utf-8') as my_file:
    my_file.writelines(num)
    my_file.seek(0)
    lines = my_file.readline()
    result = sum(map(int, lines))
    print(result)