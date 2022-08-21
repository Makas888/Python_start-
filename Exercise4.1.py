# 1. Написати програму, яка змінює значення двох цілих змінних a і b без використання додаткових змінних.
a, b = 3, 5
a, b = b, a
print(a, b)

# 2. Написати програму, яка обчислює і виводить на екран:
# • середнє арифметичне двох цілих чисел a і b;
# • середнє геометричне двох цілих чисел a і b.
a, b = 7, 5
average = (a + b) / 2
geometric_mean = (a * b) ** 0.5
print('average: ', average, '\n' + 'geometric mean: ', round(geometric_mean, 3))

# 3. Написати програму, яка переставляє цифри трьохзначного числа, яке задане користувачем
# у зворотному порядку і виводить нове число на екран.
number = 123
string_number = str(number)
print(string_number[::-1])

# 4. Написати програму, яка визначає загальну кількість годин доби (змінна hour)
# і загальну кількість хвилин доби (змінна minute), які пройшли до моменту поточної секунди доби
# (змінна second). Наприклад, якщо second = 11111 (second = 3 * 3600 + 5 * 60 + 11), то hour = 3 і minute = 5.
second = int(input('count second: '))
minute_in_hour = 60
second_in_hour = 3600
count_minute = second % second_in_hour // minute_in_hour
count_hour = second // second_in_hour % minute_in_hour
print('hour: ', count_hour, '\n' + 'minutes: ', count_minute)

# 5. Написати програму яка визначає чи є натуральне число, що ввів користувач:
# • парним;
# • таким, що закінчується на цифру 5.
number = input('enter the number: ')
if not int(number) % 2:
    print('number is even')
elif int(number) % 2:
    print('number is odd')
    if number[-1] == '5':
        print('number end is 5')

# 6. Написати програму, яка визначає значення цілої змінної number - від 1 до 7,
# в залежності від того, на який день тижня (від понеділка до неділі)
# припадає день (ціла змінна day) невисокосного року, в якому 1 січня - понеділок (1 ≤ day ≤ 365).
day = int(input('day: '))
count_days_in_week = 7
if 1 <= day <= 365:
    number = (day - 1) % count_days_in_week + 1
    print(number)
