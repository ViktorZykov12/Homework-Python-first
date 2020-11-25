with open('text3.txt', encoding='utf-8') as my_file:
    lines = my_file.readlines()
print('Сотрудники с зарплатой ниже 20 тысяч рублей: ')
sum = 0
for i in lines:
    name, zarplata = i.split()
    sum += int(zarplata)
    if int(zarplata) < 20000:
        print(name)
print(f'Средняя зарплата сотрудников: {round(sum / len(i))}')



