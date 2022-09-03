# 1)Используя словарь, напишите программу, которая выведет на экран
# название дня недели по его номеру. (1 - «Monday»)
dict_week = {'1': 'monday',
             '2': 'tuesday',
             '3': 'wednesday',
             '4': 'thursday',
             '5': 'friday',
             '6': 'saturday',
             '7': 'sunday'}
num_day = input('day of the week number: ')
res = dict_week.get(num_day, 'not correct')
print(res)

# 2)Представьте описание кота (домашнее животное) на основе словаря.
cat_data = {'name': input('name cat: '),
            'age': float(input('age: ')),
            'weight': float(input('weight: '))
            }
print_cat_data = f'The name is "{cat_data.get("name")}"\n' \
                 f'Age is {cat_data.get("age")} years\n' \
                 f'Weight is {cat_data.get("weight")} kg'
print(print_cat_data)

# 3)Напишите программу которая считает строку текста с клавиатуры и
# выведет на экран статистику, сколько раз какая буква встречается в
# этой строке. Например, для строки «Hello world» эта статистика
# выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д.
string_ = input('string: ')
char = {}
for i in string_:
    if i.isalpha():
        char[i] = string_.count(i)
        print(f'"{i}" - {char.get(i)}', end=', ')


# 4)Ввести с клавиатуры число (до миллиона), которое обозначает количество
# долларов и центов пользователя. Вывести это количество прописью.
# Например:
# How much money do you have?
# 123,34
# You have: one hundred twenty three dollars thirty four cents
num_dict = {'1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '6': 'six',
            '5': 'five',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve',
            '13': 'thirteen',
            '14': 'fourteen',
            '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen',
            '18': 'eighteen',
            '19': 'nineteen',
            '20': 'twenty',
            '30': 'thirty',
            '40': 'forty',
            '50': 'fifty',
            '60': 'sixty',
            '70': 'seventy',
            '80': 'eighty',
            '90': 'ninety'}
num = float(input('number: '))
cent = '' + str(round(num, 2))[-2:]
num = str(int(num))
res = ''
x = num
while len(num) < 6:
    num = '0' + num
if len(x) > 3:
    if num[0] != '0':
        res = res + num_dict[num[0]] + '-' + 'hundred '
    if num[1] == '1':
        res = res + num_dict[num[1] + num[2]] + ' thousand '
    elif num[1] == '0' and num[2] == '0':
        res = res + ' thousand '
    elif num[2] == '0' and num[1] != '0':
        res = res + num_dict[num[1] + '0'] + ' thousand '
    elif num[2] != '0' and num[1] == '0':
        res = res + num_dict[num[2]] + ' thousand '
    elif num[2] != 0 and num[1] != '0':
        res = res + num_dict[num[1] + '0'] + '-' + num_dict[num[2]] + ' thousand '

if num[3] != '0':
    res = res + num_dict[num[3]] + '-' + 'hundred '
if num[4] == '1':
    res = res + num_dict[num[4] + num[5]] + ' dollars '
elif num[4] == '0' and num[5] == '0':
    res = res + 'dollars '
elif num[5] == '0' and num[4] != '0':
    res = res + num_dict[num[4] + '0'] + ' dollars '
elif num[5] != '0' and num[4] == '0':
    res = res + num_dict[num[5]] + ' dollars '
elif num[5] != 0 and num[4] != '0':
    res = res + num_dict[num[4] + '0'] + '-' + num_dict[num[5]] + ' dollars '


if cent[0] == '1':
    res = res + num_dict[cent[0] + cent[1]] + ' cent'
elif cent[1] != '0' and cent[0] == '.':
    res = res + num_dict[cent[1] + '0'] + ' cent'
elif cent == '.0':
    res = res + ' 00 cent'
elif cent[0] != '0' and cent[1] == '0':
    res = res + num_dict[cent[0] + '0'] + ' cent'
elif cent[0] == '0' and cent[1] != '0':
    res = res + num_dict[cent[1]] + ' cent'
elif cent[0] != '0' and cent[1] != '0':
    res = res + num_dict[cent[0] + '0'] + '-' + num_dict[cent[1]] + ' cent'

print(res)


# 5) Напишите программу, которая переведет целое число (от 1 до 100) из
# римской записи в обычные цифры.
# Например: XXII -> 22
rim_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
r_num = input('Entered the Roman numerals: ')
res = 0
count = 0
for i in r_num:
    if len(r_num) > count + 1 and (rim_dict.get(i) - rim_dict.get(r_num[count + 1])) <= -1:
        res = res - rim_dict.get(i)
    else:
        res = res + rim_dict.get(i)
    count += 1
print(res)
