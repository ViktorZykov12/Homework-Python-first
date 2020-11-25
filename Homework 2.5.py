rating = [8,6,4,2,1]
print(rating)
new_rating = int(input('Введите значение рейтинга: '))
rating.append(new_rating)
rating.sort(reverse = True)
print(rating)