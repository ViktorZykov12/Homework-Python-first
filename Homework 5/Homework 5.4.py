with open('text4.txt') as my_file:
    lines = my_file.readlines()

dict = ('Один','Два','Три','Четыре')
new_lines = []
i = 0
for line in lines:
    less, num = line.split(' - ')
    new_lines.append(dict[i] + ' - ' + num)
    i += 1
print(new_lines)
with open('text4.1.txt', 'w+', encoding='utf-8') as new_my_file:
    new_my_file.writelines(new_lines)
