import random
from functools import reduce

lst = [2, 5, 3, 9, 4]
fruits = ["Pear", "Cucumber", "Apple", "Orange", "Guava"]

def reduce_func(acc, item):

    print(f"acc-> {acc} <> item -> {item}")
    return acc * item

from math import prod
random.shuffle(lst)
print("\n############# Reduce ############\n")


print(lst)
print(fruits)
print(reduce(reduce_func, lst))
print(sum(lst, 100))
print(prod(lst, start=100))

print("\n############# Reduce ############\n")


print(reduce(lambda acc, item: acc if acc > item else item, lst))
fruits.append("Lettuces")
print(fruits)
print(reduce(max, fruits))
print(min(lst))
print(max(lst))