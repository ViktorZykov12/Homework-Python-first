
from sys import argv

hours, rate, prize = argv[1:]
print('Выработка в часах: ', hours)
print('Ставка в час: ', rate)
print('Премия: ', prize)
print('Итого: ', int(hours)*int(rate)+int(prize))






