# def word_letters(iterable: list | str | tuple) -> dict:
#     item_dict = {}
#
#     for item in iterable:
#             if item in item_dict:
#         # item_dict[item] += 1
#              item_dict[item] + item_dict[item] + 1
#             else:
#              item_dict[item] = 1
#         # item_dict[item] = item_dict.get(item, 0) + 1
#
#         return item_dict
#
#
# print(word_letters())

# numbers = []
# for nums in numbers (2, 12):
#     numbers = [nums ** 2 for i in range(2, 12)]


#print(numbers)

# names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Rachael']
# my_names = [name for name in names if name.istitle()]
# number_of_times = int(input("how many names will you like to enter ? "))
# input_names = [input("Name?" ) for _ in range (3)]
#
# even = [even for even in range(1, 11) if even % 2 == 0]
# even_squared_odd_cubed = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 11)]
#
# print(even_squared_odd_cubed)
#
# # my_names = []
# # for name in names:
# #     if name.istitle():
# #         my_names.append(name)
#
# print(my_names)

x_and_y = []
for x in range(1, 6):
    for y in range(1, 6):
        x_and_y.append((x, y))

x_and_y = [(x, y) for x in range(1, 6) for y in range(1, 6)]
print(x_and_y)

listcomp = [num % 3 for num in range(1, 10)]
setcomp = {num % 3 for num in range(1, 6)}
dictcomp = {k: v for k, v in enumerate(range(11, 16))}
genexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(genexp), genexp)

print(next(genexp))
print(list(genexp))