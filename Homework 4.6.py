from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)



print('next')

my_list = [1, 2, 3, 4, 5, 6, 7]
count = 0
for ls in cycle(my_list):
    count += 1
    if count > 20:
        break
    print(ls)