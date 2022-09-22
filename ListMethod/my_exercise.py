
friend = ["a", [1, 2, 3], "z"]
print(friend[1][2])
# print(friend[0], [1, 1], [2])
print(friend[1][2], friend[0], friend[2])
print(friend[0] or [1, 2] or [2])

"""mutable List"""
Love = [0, 90, 27]
Love[0] = "Banke"
print(Love)

Animal = ["Hen", "Ram", "Goat", "Tiger"]
print(Animal)

import random
number = list(range(1, 17))
print(number)
random.shuffle(number)
print(number)
print(random.choice(number))

number.append([72, 73, 88])
print(number)
number.extend([99, "Olamide", "Adebayo"])
print(number)
number += ["Joy", "Love", "Wisdom"]
print(number)
number.insert(2, 0.0)
print(number)