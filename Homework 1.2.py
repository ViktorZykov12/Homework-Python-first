user_sec = int(input('Введите количество секунд: '))
hours = user_sec // 3600
min = (user_sec // 60) % 60
sec = user_sec % 60

print(hours,min,sec, sep = ':')
