# def add(x, y):
#     # assert type(x) != float
#     assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Only int or float can be added"
#     assert x > 0 and y > 0, "Numbers cannot be negative"
#     return x + y
#
#
# assert [1, 2, 3] == [1, 2, 3]
# print(add("2", "3"))
import doctest

from testing_testing.exception import MyCustomException


def add(x, y):
    """
    adds two numbers
    >>> add(10, 12)
    24
    >>> add(2, -6)
    -4
    >>> add(2, "hi")

    TypeError:

    """
    if x > y:
        raise MyCustomException("Just fooling around")
    return x + y


if __name__ == "__main__":
    doctest.testmod()
print(add(3, 4))

# print(sum(list[2, 4, 12, 3, 1, 22]))
