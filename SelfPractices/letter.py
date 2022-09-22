import string


def alphabet(letter):
    int_word = ord(letter)
    str_word = chr(int_word + 1)
    print(str_word)


user_word = str(input("Input a letter"))
alphabet(user_word)






