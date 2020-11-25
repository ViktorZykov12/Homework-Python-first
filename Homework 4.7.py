from math import factorial

def fact(n):
    for i in range(1, n+1):
        yield factorial(i)


"""
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res
        
"""

for j in fact(int(input('число: '))):
    print(j)