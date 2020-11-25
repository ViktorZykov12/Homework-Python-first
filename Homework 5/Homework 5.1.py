
with open('text1.txt', 'w+') as my_file:
    while True:
        line = input('Enter: ')
        if line == (''):
            break
        else:
            my_file.write(line + '\n')
            my_file.seek(0)
            print(my_file.read())


