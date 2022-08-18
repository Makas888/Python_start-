# 1) Написать программу, которая считает 4 числа c клавиатуры и выведет
# на экран самое большое из них.
a, b, c, d = int(input('n: ')), int(input('n: ')), int(input('n: ')), int(input('n: '))
print(max(a, b, c, d))

# Есть девятиэтажный дом, в котором 4 подъезда. Номер подъезда
# начинается с единицы. На одном этаже 4 квартиры. Напишите
# программу которая, получит номер квартиры с клавиатуры, и выведет на
# экран, на каком этаже, какого подъезда расположенна эта квартира.
# Если такой квартиры нет в этом доме, то нужно сообщить об этом
# пользователю.
flat_number = int(input('apartment number: '))
floor = 9
entrance = 4
apartments_in_floor = floor * entrance
total_apartments = apartments_in_floor * entrance
result = 1 <= flat_number <= total_apartments and \
         (f'entrance: {(flat_number - 1) // apartments_in_floor + 1}'
          f' floor: {(flat_number - 1) // entrance % floor + 1}')
print(result or 'no such apartment')

# 3) Определить количество дней в году, который вводит пользователь. В
# високосном году - 366 дней, тогда как в обычном их 365. Високосный год
# определяется по следующему правилу:
# Год високосный, если он делится на четыре без остатка, но если он
# делится на 100 без остатка, это не високосный год. Однако, если он
# делится без остатка на 400, это високосный год.
year = int(input('enter the year: '))
if year % 4 or not year % 100 and year % 400:
    print('non leap year')
else:
    print('leap year')

# 4) Треугольник существует только тогда, когда сумма любых двух его
# сторон больше третьей. Дано: a, b, c – стороны предполагаемого
# треугольника. Напишите программу, которая укажет, существует ли
# такой треугольник или нет.
side_a, side_b, side_c = float(input('side a = ')),\
                         float(input('side b = ')), \
                         float(input('side c = '))
if not bool(side_a) or not bool(side_b) or not bool(side_c):
    print("not correct")
elif side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("it's a triangle!")
else:
    print("it's not a triangle")
