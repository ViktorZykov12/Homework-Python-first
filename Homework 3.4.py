
def my_func(x, y):
    return x ** y

x = int(input('Введите положительное число: '))
y = int(input('Введите отрицательное число: '))
power = my_func(x, y)
print(power)


def my_func1(a, b):
    r = 1
    b = abs(b)
    while b > 0:
       r *= a
       b -= 1
    return 1/r

a = float(input('Введите положительное число: '))
b = float(input('Введите отрицательное число: '))
power1 = my_func1(a, b)
print(power1)