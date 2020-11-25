min_km = int(input('Сколько километров вы пробежали в первый день? '))
max_km = int(input('Цель километров: '))
day = 1
while min_km < max_km:
    min_km = min_km + ((min_km * 10) / 100)
    day += 1
print('На', day, '-й день спортсмен достигнет результата - не менее',min_km, 'км')
