def add(a: int, b: int) -> int:
    """"adds two numbers"""
    return a + b


# print(add.__name__)
# print(add.__doc__)
# print(add.__annotations__)

def operate(x, y, func):
    return func(x, y)


print(operate(2, 3, add))


# print(operate(5, 8, sub))

def multiply(a):
    def by(b):
        return a * b

    return by


multiply_by_five = multiply(5)

print(multiply_by_five(6))


def division(a):
    def by(b):
        return a / b

    return by


divide_by_twenty = division(50)
# divide_by_twenty = division(50)(5)
print(divide_by_twenty(5))

#
# def subtraction(a, b,):
#     return a - b
#
#
# print(subtraction(3 - 10))


add = lambda a, b: a + b
print(add.__name__)
print(add(10, 9))

print(add(2, 3))
print(operate(2, 3, lambda a, b: a + b))

import builtins

print(round(56.67854, 2))

arr = [1, 6, 4, 7, 2]
print(sum(arr, 100))

print(max([1, 2, 3, 4, 5, 6, 7]))

# max and indexing
fruits = "apple pear cucumber mango grape water_melon".split()
print(fruits)
print(max(fruits))
print(max(fruits, key=lambda x: x[-1]))
print(min(fruits, key=len))
print(fruits[2])

# sorted function examples
print(sorted('hello'))
print(sorted('hello', reverse=True))
print(sorted(fruits, reverse=True))

print(sorted(fruits))
print(sorted(fruits, key=len))

print(sorted('Chimamanda Adiche'))

# map function
lst = [1,2,3,4,5]
print(list(map(lambda  x: x** 2, [1,2,3,4,5])))
print([x**2 for x in lst])
print(list(map(str.upper, fruits)))
print(list(map(lambda x: x.upper(), fruits)))

fruits.append('Agbado')
print(fruits)
print(list(filter(str.istitle, fruits)))
print(list(filter(lambda x: not x.istitle(), fruits)))

from functools import reduce

print(reduce(lambda acc, item: acc + item, lst))
