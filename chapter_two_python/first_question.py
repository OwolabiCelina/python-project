
# x = 2
# y = 3
#
# print('x =', x)
# print('Value of', x, '+', x, 'is', (x + x))
# print((x + y), '=', (y + x))
#
# print("\n========================================\n")
#
# rating = input('Enter an integer rating between 1 and 10')
# print(rating)
# print("\n=========================================\n")
#
# grade = int(input("Enter your grade"))
# if grade >= 90:
#     print('Congratulations! Your point of 91 earns you an A in this course!')
#
# print("\n=====================================\n")
# num = 27.5 + 2
# n = 27.5  * 2
# print(num)
# print(n)

print("\n==============================")
#
#
# radius = int(input("Enter radius: "))
# diameter = 2 * radius
# circumference = 2 * 3.14159 * radius
# area = 3.14159 * radius * radius
#
# print('diameter is: ', diameter, 'circumference is: ', circumference, 'area is: ', area)
print("\n=================================\n")
#
# num1 = int(input("Enter first integer"))
# num2 = int(input("Enter second integer"))
# num3 = int(input("Enter third integer"))
#
# addition =  num1 + num2 + num3
# average = 0
#
# print(addition)
# print(average(num3, num2, num1))
# print(max(addition))
# print(min(addition))
import math
even = 0
odd = 0

numbers = [23, 2, 4, 11, 13, 15, 12, 98, 1002, 1045, 10000, 1028, 2042, 2334, 3490, 8873, 30022]
lst = []
result = 1
for number in numbers:
    if number % 2 != 0:
        lst.append(number)
for numb in lst:
    print(numb)
    result *= numb

print(result)

#     if number % 2 == 1 & number ** 2:
#         lst.append(number)
# print(number)
#
#
# print("\n========================\n")
# import itertools
# numbers = [23, 2, 4, 11, 13, 15, 12, 98, 1002, 1045, 10000, 1028, 2042, 2334, 3490, 8873, 30022]
# lst = []
# for number in numbers:
#     lst.append(number)
# print(min(lst))
# print(max(lst))
# if number % 2 == 1 & number ** 2:
#     lst.append(number)
# print(number)

# print(10, 30, 40, sep=' ')

print("\n=======================\n")
# total = 0
# for num in range(1000001):
#     # print(num)
#     total = total + num
# print(total)

print("\n=====================\n")
total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade
    grade_counter += 1

average = total / grade_counter
print(f'Class average is {average}')