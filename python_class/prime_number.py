number = int(input("Enter any number: "))

fact = 0

for i in range(number, 0, -1):
    if number % i == 0:
        fact += 1
if fact == 2:
    print("Number is a prime number")
else:
    print("Number is not prime")
