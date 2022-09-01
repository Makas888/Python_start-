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
