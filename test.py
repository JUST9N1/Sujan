import random

def guess(x):
    count = 0
    random_number = random.randint(1, x)
    guess = 0
    while random_number != guess:
        count += 1
        guess = int(input("Enter a number between 1 and {}".format(x)))
        if guess < random_number:
            print("Number is too low")
        elif guess > random_number:
            print("Number is too high")
        else:

            print(f"You've Guessed the number in {count} times. \nCongratulation!")

choice = int(input("Enter a number: "))
guess(choice)

