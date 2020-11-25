def my_func(user_num1, user_num2):
    try:
        return user_num1 / user_num2
    except ZeroDivisionError:
        print('Деление на 0 запрещено!')
        
user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))
result = my_func(user_num1, user_num2)
print(result)




