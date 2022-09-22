

print("########### match ##########")

# num = int(input("Enter a number"))
#
# match num:
#     case _ as x if 1 <= 1 or x <= 10:
#         print(x)
#
#     case _ as x if 1 <= 11 or x <= 20:
#         print(x)
#
#     case 30 | 40 | 50:
#         print(x)
#
#     case _:
#         print("Don't know you")
# #
# lst = [20, 13, 16]
#
# match lst:
#
#     case[i1, i2, i3]:
#         print(i3, i2, i1)
#
#     case _:
#         print("Nothing matched")
#
#  d = {
#      "name": "Banke",
#      "age": 18,
#      "is_swit": True
#  }
#
# match d:
#      case{"name": str(name), "age": int()}:
#          print(name)
#
#      case _:
#         print("Nothing to match")
#
# def fizzBuzz(num):
#     three = num % 3
#     five = num % 5

# match (three, five):
#         return "FizzBuzz"
#     case(0, 0):
#         return "Fizzbuzz"
#     case (0, _):
#         return "Fizz"
#     case (_, 0):
#         return "Buzz"
#     case_:
#         return num
#
# for i in range(1, 101):
#     print(fizz_buzz(i))
#
#
def summing_list(list: list[int]) -> int| None:
        match list:
            case[]:
                return 0

            case[first_value, * another_list]:
                return first_value + summing_list(another_list)

            case _:
                print("Can only accept an int")
                return None
print(summing_list([1, 2, 3, 4, 5]))


import itertools
print(summing_list([1, 2, 3, 4, 5, 6, 7, 8]))
print(list(itertools.zip_longest([1, 2], [3, 4, 5], [6, 7, 8], fillvalue=0)))
