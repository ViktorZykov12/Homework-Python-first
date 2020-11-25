def my_func(a,b,c):
    return max(a+b, max(b+a, b+c))

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
max_num = my_func(a,b,c)

print(max_num)