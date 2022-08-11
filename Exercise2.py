number = int('123')     #1

number = float(number)   #2

int_number = int(12.345)   #3

card_number = '5168755634239889'    #4
print(card_number[-4:])

x = 154                       #5
num = str(x)
summ = 0
for i in num:
    summ += int(i)
print(summ)

import math                    #6
a = 4
b = 6
c = 7
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'area of a triangle: {s}')

x = 15468943345                       #7
num = str(x)
summ = 0
for i in num:
    summ += int(i)
print(summ)

number = 56905                        #8
number_str = str(number)
print(f'number of digits {len(number_str)}')

number = 12345                           #9
number = str(number)
print(number[::-1])
