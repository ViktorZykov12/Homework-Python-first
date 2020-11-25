
def my_func():
    my_str = 'Введите числа, разделенных пробелом. Для выхода введите любой символ: '
    sum = 0
    while True:
        try:
            for i in map(int, input(my_str).split()):
                sum += i
            print(sum)
        except ValueError:
            return print(sum)


my_func()

