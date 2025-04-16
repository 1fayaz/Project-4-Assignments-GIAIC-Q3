# Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

# ===================================================================================


import random

SIDES_ON_DICE = 6

def roll_two_dice():
    
    first_roll = random.randint(1, SIDES_ON_DICE)
    second_roll = random.randint(1, SIDES_ON_DICE)
    combined = first_roll + second_roll

    print(f"Each die has {SIDES_ON_DICE} sides.")
    print(f"You rolled: {first_roll} and {second_roll}")
    print(f"The sum of both rolls is: {combined}")


if __name__ == "__main__":
    roll_two_dice()