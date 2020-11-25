my_dict = dict()
with open('text6.txt', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    for line in lines:
        splited_lines = line.split()
        subj = splited_lines[0]
        sum_less = sum([int(x[:x.find('(')]) for x in splited_lines[1:] if '(' in x])
        my_dict[subj[:-1]] = sum_less
print(my_dict)