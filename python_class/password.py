import string

word = input("Enter your password ")

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

special_characters = "@#$%!^&*()-+"

validation = False

if any(case in numbers for case in word):
    print("You have at Least One digit")
    validation = True

if any(case in lower_case for case in word):
    print("You have at Least one lower_case")
    validation = True

if any(case in upper_case for case in word):
    print("You have at Least one upper_case")
    validation = True

if any(case in special_characters for case in word):
    print("You have at least one special_character")
    validation = True

else:
    print("Password has been generated successfully")
    validation = True


