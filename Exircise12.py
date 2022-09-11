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


def age_correct(age):
    return True if 0 < age < 500 else False


def age_gradation(age, name):
    if age_correct(age):
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
    start = ''
    for i in a:
        start += str(i)
    return int(start)


def max_combination(a):
    finish = ''
    for i in reversed(a):
        finish += str(i)
    return int(finish)


def all_combination(a):
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
