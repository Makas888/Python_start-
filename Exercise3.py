#  1. Write a Python program to print the number entered by user only if the number entered is negative.
number = float(input('enter the number: '))
print('number is positive:', number >= 0)

#  2. Write a Python program to check if the value a is less than 20 or not.
value = float(input('enter the value: '))
print('value < 20 :', not value > 20)

#  3. Write a Python program to check if a given number is Zero or Not.
given_number = float(input('number: '))
print('number is zero:', given_number == 0 or given_number < 0 < given_number)

#  4. Write a Python program to check if a given number is Even or Odd.
odd_even = float(input('enter the number: '))
print('number is even:', odd_even % 2 == 0)

#  5. Write a Python program to find largest number among three numbers entered by user.
numbers = input('enter 3 numbers: ')
print('entered numbers', numbers, 'equal numbers:', max(numbers))
