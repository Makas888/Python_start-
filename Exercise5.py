# 1)Выведите на экран все числа в диапазоне от 1 до 100 кратные 7.
range_ = range(1, 101)
multiples = 7
[print(number) for number in range_ if not number % multiples]

# 2)Вычислить с помощью цикла факториал числа n введенного с
# клавиатуры (4<n<16). Факториал числа - это произведение всех чисел от
# этого числа до 1. Например, 5!=5*4*3*2*1=120
number = int(input('n: '))
factorial = number
if 4 < number < 16:
    while number > 1:
        number -= 1
        factorial = factorial * number
    print('factorial n: ', factorial)
else:
    print('not a valid number')

# 3)Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
# = 5, 2 x 5 = 10, а не просто 5, 10 и т. д.
# 3)Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
# = 5, 2 x 5 = 10, а не просто 5, 10 и т. д.
factor = 5
factor_2 = 1
while factor_2 <= 10:
    result = factor * factor_2
    print(factor, 'x', factor_2, '=', result)
    factor_2 += 1

factor = 1
factor_2 = 1
for _ in range(10):
    while factor < 10:
        factor += 1
        result = factor * factor_2
        print(factor, 'x', factor_2, '=', result, sep='', end='\t')
    factor = 1
    factor_2 += 1
    print('')

# 4)Выведите на экран прямоугольник из *. Причем, высота и ширина
# прямоугольника вводятся с клавиатуры. Например, ниже представлен
# прямоугольник с высотой 4 и шириной 5.
height = int(input('height: '))
width = int(input('width: '))
count = 0
for i in range(height):
    count += 1
    if count == 1 or count == height:
        print('*' * width)
    elif 1 < count < height:
        print('*', ' ' * (width - 4), '*')
