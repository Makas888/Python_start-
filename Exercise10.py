# 1) Напишите функцию, которая вернет максимальное число из списка
# чисел.
def max_number(numbers):
    return max(numbers)


# 2) Реализуйте функцию, параметрами которой являются - два числа и
# строка. Возвращает она конкатенацию строки с суммой чисел.
def summa(a, b, string):
    return str(a + b) + string


# 3) Реализуйте функцию рисующую на экране прямоугольник из звездочек
# «*». Ее параметрами будут целые числа, которые описывают длину и
# ширину такого прямоугольника.
def rectangle(height, width):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print('*' * width)
        else:
            print(f'*{" " * (width - 2)}*')


# 4) Напишите функцию, которая реализует линейный поиск элемента в
# списке целых чисел. Если такой элемент в списке есть, то верните его
# индекс, если нет, то верните число «-1».
def search_elem(numbers, item):
    return numbers.index(item) if item in numbers else '-1'

# 5) Напишите функцию, которая вернет количество слов в строке текста
def count_word(text):
    return len(text.split())

# 2) Число-палиндром с обеих сторон (справа налево и слева направо)
# читается одинаково. Самое большое число-палиндром, полученное
# умножением двух двузначных чисел: 9009 = 91 × 99. Найдите самый
# большой палиндром, полученный умножением двух трехзначных чисел.
# Выведите значение этого палиндрома и то, произведением каких чисел он
# является.
def palindrome(def palindrome(a, b):
    palindromes = []
    for j in range(a, 1, -1):
        for i in range(b, 1, -1):
            if str(j * i) == str(j * i)[::-1]:
                palindromes.append([j * i, j, i])
    res = max(palindromes)
    return res


result = palindrome(999, 999)
print(f'{result[0]} - is max palindrome of {result[1]} and {result[2]}')
print(palindrome(999, 999))
