def find_max(array):

    ele = array[0]
    for num in array:
        if num > ele:
            ele = num

    return ele

largest = [10, 23, 11, 22, 50, 19]
# result = array
print(find_max(largest))


#             min = arr[0]
#             for number in arr:
#                 if number > min:
#                     sum = number
#
#             return number
#
# minimum = []
