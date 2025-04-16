# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# ====================================================================================================================



import random

def guess_the_number():
    number_to_guess = random.randint(1, 99)
    print("Guess the number I'm thinking of (between 1 and 99)...")

    user_try = int(input("Your guess: "))

    while user_try != number_to_guess:
        if user_try < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        print()  # For spacing
        user_try = int(input("Try again: "))

    print(f"Nice! You got it. The number was {number_to_guess}.")

if __name__ == '__main__':
    guess_the_number()
