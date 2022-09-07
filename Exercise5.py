import random
import numpy

# 1)Выведите на экран все числа в диапазоне от 1 до 100 кратные 7.
[print(number, end=' ') for number in range(7, 100, 7)]

# 2)Вычислить с помощью цикла факториал числа n введенного с
# клавиатуры (4<n<16). Факториал числа - это произведение всех чисел от
# этого числа до 1. Например, 5!=5*4*3*2*1=120
number = int(input('n: '))
if 4 < number < 16:
    for i in range(2, number):
        number *= i
    print('factorial n: ', number)
else:
    print('not a valid number')

# 3)Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
# = 5, 2 x 5 = 10, а не просто 5, 10 и т. д.
# 3)Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
# = 5, 2 x 5 = 10, а не просто 5, 10 и т. д.
for i in range(1, 11):
    print(i, 'X', 5, '=', i * 5)

for i in range(1, 11):
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)

# 4)Выведите на экран прямоугольник из *. Причем, высота и ширина
# прямоугольника вводятся с клавиатуры. Например, ниже представлен
# прямоугольник с высотой 4 и шириной 5.
height, width = int(input('height: ')), int(input('width: '))
res = '*' * width + '\n'
res += ('*' + ' ' * (width - 2) + '*\n') * (height - 2)
res += '*' * width + '\n'
print(res)

# 5)Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.
list_numbers = [random.randrange(0, 100) for _ in range(20)]
count = 0
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
base_list = [random.randrange(20) for _ in range(4)]
new_list = base_list.copy() + [i * 2 for i in base_list]
print(base_list, new_list, sep='\n')

# 7)Создайте список из 12 элементов. Каждый элемент этого списка представляет собой
# зарплату рабочего за месяц (случайное число от 7500 до 15000 грн.). Выведите этот
# список на экран и вычислите среднемесячную зарплату этого рабочего.
salary_list = [random.randint(7500, 15000) for _ in range(12)]
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
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_new = numpy.array(matrix, numpy.int_)
summa_numbers_in_new_matrix = sum(sum(matrix_new))
print(matrix_new, 'summa = ', summa_numbers_in_new_matrix)

# 1)С помощью циклов вывести на экран все простые числа от 1 до 100. Простое число —
# число, которое делится нацело только на единицу или само на себя. Первые простые
# числа это — 2,3,5,7…
number = 0
while number < 100:
    number += 1
    count = 2
    while count < number:
        if not number % count:
            break
        count += 1
    else:
        print(number)

# 2)Выведите на экран «песочные часы», максимальная ширина которых считывается с
# клавиатуры (число нечетное). В примере ширина равна 5.
# *****
#  ***
#   *
#  ***
# *****
watch_width = int(input('set lock width,  odd number: '))
if watch_width % 2 and watch_width > 2:
    count_ = 0
    for i in range(watch_width, 0, -2):
        print(' ' * count_ + i * '*')
        count_ += 1
    for j in range(3, watch_width + 1, 2):
        print(' ' * (count_ - 2) + j * '*')
        count_ -= 1
else:
    print('number is not odd or not positive, repeat please')

# 3)Написать код для зеркального переворота списка [7,2,9,4] -> [4,9,2,7].
# Список может быть произвольной длины. (При выполнении задания
# использовать дополнительный список нельзя).
list_ = [7, 2, 9, 4]
list_.reverse()
print(list_)

# 4)«Перевернуть матрицу». Т.е. написать программу, которая повернет базовую
# матрицу на 90,180,270 градусов по часовой стрелке. (При выполнении задания
# использовать дополнительную матрицу нельзя).
matrix = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
[print(i) for i in matrix]
print('')
# 90'
for i in range(len(matrix)):
    a = len(matrix) - 1
    for j in range(len(matrix)):
        matrix[i].append(matrix[a][0])
        matrix[a].pop(0)
        a -= 1
[print(i) for i in matrix]
print('')
# 180'
matrix = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
[i.reverse() for i in matrix]
[print(i) for i in matrix]
print('')
# 270'
matrix = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
for i in range(len(matrix)):
    a = len(matrix) - 1
    for j in range(len(matrix)):
        matrix[i].append(matrix[a][0])
        matrix[a].pop(0)
        a -= 1
matrix.reverse()
[print(i) for i in matrix]
