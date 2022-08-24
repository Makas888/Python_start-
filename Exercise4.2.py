# 1) Дано число. Проверить, является ли оно «счастливым билетом».
# Примечание: счастливым билетом называется число, в котором, при четном
# количестве цифр в числе, сумма цифр его левой половины равна сумме цифр его
# правой половины. Например, рассмотрим число 1322. Его левая половина равна
# 13, а правая 22, и оно является счастливым билетом (т. к. 1 + 3 = 2 + 2).
number = input('number: ')
list_number = list(map(int, number))
# list_number = [int(i) for i in number]
# for i in number:
#     list_number.append(int(i))
if not len(list_number) % 2:
    half_list = len(list_number) // 2
    if sum(list_number[:half_list]) == sum(list_number[half_list:]):
        print('lucky ticket')
    else:
        print('not lucky ticket')
else:
    print('not lucky ticket')

# 2)С клавиатуры вводится шестизначное число. Проверить, является ли оно
# палиндромом. Примечание: палиндромом называется число, слово или
# текст, которые одинакового читаются слева направо и справа налево.
# Например, это числа 143341, 5555, 7117 и т. д.
palindrome = input('Enter the word or number: ')
if palindrome == palindrome[::-1]:
    print('palindrome')
else:
    print('not palindrome')

# 3) Есть круг с центром в начале координат и радиусом 4. Пользователь вводит с
# клавиатуры координаты точки x и y. Написать программу, которая определит,
# лежит ли эта точка внутри круга или нет.
x = int(input('x: '))
y = int(input('y: '))
r = 4
if pow(x, 2) + pow(y, 2) <= pow(r, 2):
    print('yes')
else:
    print('no')

# 4) Дан треугольник координаты вершин которого А(0,0), В(4,4), С(6,1). Пользователь
# вводит с клавиатуры координаты точки x и y. Написать программу, которая
# определит, лежит ли эта точка внутри треугольника или нет.
x_o, y_o = int(input('X:')), int(input('Y:'))
x_a, x_b, x_c = 0, 4, 6
y_a, y_b, y_c = 0, 4, 1
s_abc = int(abs((x_a - x_c) * (y_b - y_c) - (x_b - x_c) * (y_a - y_c)) / 2)
s_abo = int(abs((x_a - x_o) * (y_b - y_o) - (x_b - x_o) * (y_a - y_o)) / 2)
s_aoc = int(abs((x_a - x_c) * (y_o - y_c) - (x_o - x_c) * (y_a - y_c)) / 2)
s_boc = int(abs((x_o - x_c) * (y_b - y_c) - (x_b - x_c) * (y_o - y_c)) / 2)
if s_abo + s_aoc + s_boc == s_abc:
    print('yes')
else:
    print('no')
