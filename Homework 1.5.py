proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if proceeds > costs:
    print('Выручка больше издержек')
    profit = proceeds - costs
    print('Прибыль составит: ', profit)
    rent = profit/proceeds
    print('Рентабельность: ', rent)
    workers = int(input('Введите количество работников: '))
    profit_workers = profit/workers
    print('Прибыль на одного сотрудника составит: ', profit_workers)
else:
    print('Издержки больше выручки')