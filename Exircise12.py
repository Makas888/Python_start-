# 1) Напишите функцию, которая вернет сумму всех нечетных элементов списка.
# Например, для списка вида [2,1,4,6,3] ваша программа должна вернуть 4.
def max_even(a: list):
    return sum([i for i in a if i % 2])


numbers = [2, 1, 4, 6, 3]
print(max_even(numbers))

# 2) Напишите функцию, которая будет рисовать на экране треугольник заданной
# высоты. Символ, которым рисуется треугольник, также должен быть параметром
# этой функции. Например, если в качестве параметра задать величину высоты
# равную 5, а символ равным «#», то результат должен быть такой:
# #
# ##
# ###
# ####
# #####


def triangle(height: int, symbol: str):
    res = ''
    for item in range(1, height + 1):
        res += str(symbol * item) + '\n'
    return res


print(triangle(5, '#'))

# 3) Напишите программу, которая попросит ввести пользователя его имя и возраст.
# После проверки возраста на корректность (чтобы не был меньше 0 и больше 500)
# выведите имя человека и его возрастную градацию:
# 0-10 — детский возраст, 10-25 - юный возраст, от 25 до 44 лет - молодой возраст,
# 44-60 лет - средний возраст, 60-75 лет - пожилой возраст, 75-90 лет - старческий
# возраст, а после 90 - долгожитель.


def age_gradation(age, name):
    if 0 < age < 500:
        if 0 < age <= 10:
            return f'{name}, {age} years - "childhood"'
        if 10 < age <= 25:
            return f'{name}, {age} years - "teenager"'
        if 25 < age <= 44:
            return f'{name}, {age} years - "young age"'
        if 44 < age <= 60:
            return f'{name}, {age} years - "average age"'
        if 60 < age <= 75:
            return f'{name}, {age} years - "elderly age"'
        if 75 < age <= 90:
            return f'{name}, {age} years - "old age"'
        if 90 < age:
            return f'{name}, {age} years - "long - liver"'
    else:
        return 'age is not correct'


first_name, age_ = input('name: '), int(input('age: '))
print(age_gradation(age_, first_name))

# 1*) Существует список [1,2,3,4,5]. Размер списка может быть произвольным, однако
# заполнен он всегда цифрами от 1 и далее по возрастанию с шагом 1. Напишите
# программу, которая выведет на экран все возможные комбинации, которые могут
# быть получены перестановкой элементов этого списка. Внимание! Повторений и
# пропущенных комбинаций быть не должно.


def min_combination(a):
    """
    minimum number
    will return the minimum number from the digits in the list
    :param a: list
    :return: int
    """
    start = ''
    for i in a:
        start += str(i)
    return int(start)


def max_combination(a):
    """
    max number
    will return the maximum number from the digits in the list
    :param a: list
    :return: int
    """
    finish = ''
    for i in reversed(a):
        finish += str(i)
    return int(finish)


def all_combination(a):
    """
    returns a list with all possible combinations of numbers contained in the list
     from 1 and then in ascending order with a step of 1 passed to the function
    :param a: list
    :return: list
    """
    if not isinstance(a, list):
        return None
    for i in a:
        if not isinstance(i, int):
            return None
    if not a == list(range(1, len(a) + 1)):
        return None
    set_num = set(a)
    res = []
    for item in range(min_combination(a), max_combination(a) + 1):
        res_n = []
        for n in str(item):
            res_n.append(int(n))
        set_n = set(res_n)
        if set_n == set_num:
            res.append(res_n)
    return res


x = [1, 2, 3, 4, 5]
print(all_combination(x))

# 2*)
# ☺
# 7
# 5 8
# 9 8 2
# 1 3 5 6
# 6 2 4 4 5
# 9 5 3 5 5 7
# 7 4 6 4 7 6 8
# На вершине горы стоит золотоискатель (смайлик
# наверху). Цифра в клетке обозначает количество
# золотых слитков, которые в ней хранятся.
# Золотоискатель может за один раз или спуститься на
# одну клетку вниз, или спуститься на одну клетку вниз и
# вправо.
# Напишите программу, которая определит
# максимальное количество золотых слитков, которые
# может найти золотоискатель, двигаясь от вершины горы
# вниз.
import random


def max_gold(args):
    """
    return the max amount in the task
    returns the sum of the numbers of the most profitable passage of the
     sequence according to the conditions of the "gold digger" problem
    :param args: str
    :return: int
    """
    if not isinstance(args, str):
        return None
    args = args.replace(' ', '').split('\n')
    args.remove(args[0])
    max_count_gold = 0
    count = 0
    for arg in args:
        if len(arg) > 1:
            max_count_gold += max(int(arg[count]), int(arg[count + 1]))
            if int(arg[count]) == int(arg[count + 1]) and len(arg) < len(args) - 1:     # line of code "gold digger's intuition 1 step ahead"
                if max(int(args[len(arg)][count + 1]), int(args[len(arg)][count + 2]),  #
                       int(args[len(arg)][count])) == int(args[len(arg)][count + 2]):   #
                    count += 1                                                          #
            elif max(int(arg[count]), int(arg[count + 1])) == int(arg[count + 1]):
                count += 1

        elif len(arg) == 1:
            max_count_gold += int(arg[0])
    return max_count_gold


res = '☺'
for item in range(1, 8):
    res += '\n'
    for i in range(item):
        res += str(random.randint(1, 9)) + ' '
    res = res.rstrip()

print(res)
print(f'Gold digger mined {max_gold(res)} gold bars')

# 1) Существуют такие последовательности чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реализуйте программу, которая выведет следующий член этой последовательности
# (либо подобной им) на экран. Последовательность пользователь вводит с
# клавиатуры в виде строки. Например, пользователь вводит строку 0,5,10,15,20,25 и
# ответом программы должно быть число 30.
def is_arithmetic_progressive(a):
    for j in range(1, 10):
        if a == [i for i in range(a[0], a[-1] + j, j)]:
            return a[len(a) - 1] + j
    else:
        return False


def is_geometric_progressive(a):  # 1,2,4,8,16,32
    for j in range(2, 10):
        if a[1:] == [a[i] * j for i in range(len(a) - 1)] and a[0] == a[1] / j:
            return a[len(a) - 1] * j
    else:
        return False


def is_power_progressive(a):  # 1,4,9,16,25
    for j in range(2, 10):
        if a == [i ** j for i in range(a[0], len(a) + 1)]:
            return (len(a) + 1) ** j
    else:
        return False


def next_elem_sequence(a):
    if not isinstance(a, list):
        return None
    for i in a:
        if not isinstance(i, int):
            return None
    if is_arithmetic_progressive(x):
        return is_arithmetic_progressive(x)
    if is_geometric_progressive(x):
        return is_geometric_progressive(x)
    if is_power_progressive(x):
        return is_power_progressive(x)
    else:
        return f'{a} is not sequence'


x = input('enter: ')
x = [int(i) for i in x.split(',')]
print(next_elem_sequence(x))
