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

# 1) Существует список [1,2,3,4,5]. Размер списка может быть произвольным, однако
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
