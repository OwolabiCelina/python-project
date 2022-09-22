import random

lst = list(range(1, 11))
print(lst)
random.shuffle(lst)

print(lst)
#
# lst.append([20, 30, 40])
# print(lst)
# lst.extend([20,30,40])
# print(lst)

lst += [20, 30, 40]

lst.insert(-1, 56)
print(lst)

last_item = lst.pop()
print(last_item)
print(lst)

item_at_index_0 = lst.pop(0)
print(lst)

print("Count", lst.count(8))
lst.remove(8)
print(lst)

# del lst
# # lst.clear()
# print(lst)
# print(lst.index(3))

lst.insert(2,[3,4])
lst.reverse()
print(lst)

# s = "Write a sentence and reverse it"
# s_list = s.split()
# s_list.reverse()
# print(" ".join(s_list))
#
# lst.sort(reverse=True)
# print(lst)

def last_elem(string):
    return string[-1]

fruits = ["Banana","Apple","cucumber","mango","grape"]
fruits.sort(key=last_elem, reverse=True)
print(fruits)

