import string

word = input("What would you like to encode: ")
key = int(input("your key "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_letters_code = upper_letters[key:] + upper_letters[:key]

letters = lower_letters + upper_letters
letters_code = lower_letters_code + upper_letters_code

encoded_word = word.translate(str.maketrans(letters, letters_code))

print(word)
print(encoded_word)


# print("Now, is the brute force approach")

decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))

print(decoded_word)

for i in range(1, 27):
    lower_letters = lower_letters[i:] + lower_letters[:i]
    upper_letters = upper_letters[i:] + upper_letters[:i]

    letters = lower_letters + upper_letters
    letters_code = lower_letters_code + upper_letters

    print(encoded_word.translate(str.maketrans(letters_code, letters)))
