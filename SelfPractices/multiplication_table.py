# def largest_num(number):
#     return number
#
#
# num = largest_num([2000, 11, 5, 88, 90, 1000])
# print(max(num))
# print(sorted(num))
# print(callable(max(num)))


# def add(a, b):
#     return a + b
#
#
# # def sum():
# #     add(2, 5)
# total = add(2, 5)
#
#
# print(add(2, 5))
#
def add(a, b, c):
    return a * b * c


def multiply(num1, num2):
    return num1 * num2


def subtraction(first_num, second_num):
    return first_num - second_num


def total():
    # a = 5
    # b = 6
    # c = 3

    add(5, 6, 3)
    multiply(4, 5)
    subtraction(20, 5)

    k = add(5, 6, 3)
    sum1 = multiply(4, 5)
    sum2 = subtraction(20, 5)


print(add(5, 6, 3))
print(multiply(4, 5))
print(subtraction(20, 5))
