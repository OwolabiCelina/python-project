from ListMethod import practice10

random_number: int = random.randint(0, 100)

counter = 0

while counter < 3:

    guess_number = int(input("Enter a number: "))

    if guess_number == random_number:
        print("guess is accurate")

    elif guess_number < random_number:
        print("guess is too low, try again")

    elif guess_number > random_number:
        print("guess is too high")

    counter+=1

print("Trial time is up")
