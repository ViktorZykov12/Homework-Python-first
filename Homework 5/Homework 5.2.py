with open('text2.txt', encoding='utf-8' ) as my_file:
    lines = my_file.readlines()
    print('В файле содержтся строк: ', len(lines))

    for i, line in enumerate(lines, 1):
        print(f'В {i} строке {len(line.split())} слов')
