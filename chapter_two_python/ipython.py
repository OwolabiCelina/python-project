# num = 10 / 3
# print(num)
#
# print("\n###############\n")
#
# n = 10 / 3 + 7
# y = 10 / (3 + 7)
# i = 10 / 3 - 3
# print(n)
# print(y)
# print(i)
#
# print("\n***********\n")
#
# name = print("what's your name? ")
# print(name)

print("Enter two integers, and I will tell you the relationships they satisfy")
print("\n=========================================\n")

number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))

if number1 == number2:
    print(number1, 'is equal to', number2)
if number1 != number2:
    print(number1, 'is not equal to', number2)
if number1 < number2:
    print(number1, 'is less than', number2)
if number1 > number2:
    print(number1, 'is greater than', number2)
if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)

print("\n==================================================\n")

number1 = int(input("Enter first integer"))
number2 = int(input("Enter second integer"))
number3 = int(input("Enter third integer"))

minimum = number1


if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print('minimum value is', minimum)