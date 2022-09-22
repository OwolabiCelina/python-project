# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#
#     return smallest_index
#
#
# print(find_smallest([5, 6, 1, 3, 2]))
#
#
# def select_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest = find_smallest(arr)
#         new_arr.append(arr.pop(smallest))
#     return new_arr
#
#
# print(select_sort([5, 3, 6, 2, 10, 4, 7, 8, 9]))
#

def largest_number(numbers):
    counter = []
    largest = 0

    for number in numbers:
        if number > largest:
            largest = number
            counter.append(largest)

    return largest


lst = [10, 20, 3, 5, 9, 15]
lst.sort()
print(lst)

print(largest_number([10, 20, 3, 5, 9, 15]))

# print(int(False))

# i = int(True)
# j = int(False)
#
# print(i)
# print(j)