# 1)Выведите на экран все числа в диапазоне от 1 до 100 кратные 7.
range_ = range(1, 101)
multiples = 7
[print(number, end=' ') for number in range_ if not number % multiples]

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

# 5)Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.
import random
list_numbers = []
count = 0
[list_numbers.append(random.randrange(0, 100)) for _ in range(20)]
for i in list_numbers:
    if i % 2:
        count += 1
print(list_numbers)
print('odd numbers: ', count)

# 6)Создайте список случайных чисел (размером 4 элемента). Создайте второй список в
# два раза больше первого, где первые 4 элемента должны быть равны элементам
# первого списка, а остальные элементы заполните удвоенными значением начальных.
# Например,
# Было → [1,4,7,2]
# Стало → [1,4,7,2,2,8,14,4]
import random
base_list = []
[base_list.append(random.randrange(20)) for _ in range(4)]
new_list = base_list.copy()
[new_list.append(base_list[i] * 2) for i in range(4)]
print(base_list)
print(new_list)

# 7)Создайте список из 12 элементов. Каждый элемент этого списка представляет собой
# зарплату рабочего за месяц (случайное число от 7500 до 15000 грн.). Выведите этот
# список на экран и вычислите среднемесячную зарплату этого рабочего.
import random
import numpy
salary_list = []
[salary_list.append(random.randint(7500, 15000)) for _ in range(12)]
average_salary = int(numpy.mean(salary_list))
print(salary_list)
print('Average salary: ', average_salary)

# 8)Представьте в виде списка списков матрицу
# [ 1, 2 , 3, 4]
# [ 5, 6 , 7, 8]
# [ 9,10, 11, 12]
# [13,14, 15, 16]
# Напишите программу, которая выведет эту матрицу на экран, вычислит и выведет
# сумму элементов этой матрицы.
import numpy
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_new = numpy.array(matrix, numpy.int_)
summa_numbers_in_new_matrix = sum(sum(matrix_new))
print(matrix_new, 'summa = ', summa_numbers_in_new_matrix)
