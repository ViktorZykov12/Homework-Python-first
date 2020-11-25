user_num = int(input('Введите номер месяца от 1 до 12: '))
season = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for key, value in season.items():
    if user_num in value:
        print(key)

