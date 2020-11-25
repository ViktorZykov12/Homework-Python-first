from functools import reduce


my_list = [i for i in range(100, 1001, 2) ]
def my_func(x, y):
    return x*y

print(reduce(my_func, my_list))

#print(reduce(lambda x, y: x * y, my_list))