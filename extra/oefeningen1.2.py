import random
min=1
max=100
number = random.randint(min, max)

print("Welcome to the Number Guessing Game! I'm thinking of a number between ", min ," and " , max , "try to guess it.")
guess = input("enter your choice: ")

def guess(guess):
    while guess:
        if int(guess) == number:
            print("Congratulations! You guessed the correct number.")
        elif int(guess) < number:
            print("Sorry, you guessed too low. Try again.")
            guess = input("enter your new choice: ")
            round(guess)
        else:
            int(guess) > number
            print("Sorry, you guessed too high. Try again.")
            guess = input("enter your new choice: ")
            round(guess)
guess(guess)