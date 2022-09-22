
#number = int(input("number, position"))

def get_digit(number, position):


    ''':return digit at position in number, counting from right'''

    return number// (10**position)%10
print(get_digit(123456, 2))

#def get_length(number: int) -> int:
 #   return len(str(number))