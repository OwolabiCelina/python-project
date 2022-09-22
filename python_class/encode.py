import string

word = input("What would you like to encode")

key = int(input("Your key ?"))

lower_letters = string.ascii_lowercase

upper_case = string.ascii_uppercase

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_case_code = upper_case[key:] + upper_case[:key]

letters = lower_letters + upper_case
letters_code = lower_letters_code + upper_case_code

#print(letters)
#print(letters_code)

encoded_word = word.translate(str.maketrans(letters, letters_code))

#print(word)
print(encoded_word)

""""decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))
print(decoded_word)

print("Now, the brute force approach")
for i in range(1, 27):
    lower_letters_code = lower_letters[i:] + lower_letters[:i]
    upper_case_code = upper_case[i:] + upper_case[:i]
    
    letters = lower_letters + upper_case
    letters_code = lower_letters_code + upper_case_code
    print(encoded_word.translate(str.maketrans(letters_code, letters)))"""