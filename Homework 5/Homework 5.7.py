import json

firm_dict = {}
average_profit = []

with open('text7.txt', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)
average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'Средняя прибыль:', average_profit}]

with open('text7.json', 'w') as f_json:
    json.dump(out_info, f_json)
with open('text7.json') as f_json:
    print(json.load(f_json))
