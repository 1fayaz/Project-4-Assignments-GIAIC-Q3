# Description:
# This script simulates rolling two dice three times and displays the outcome of each roll.
# It also demonstrates the concept of variable scope in Python.

import random

SIDES_ON_DIE = 6

def simulate_roll():
    first_die = random.randint(1, SIDES_ON_DIE)
    second_die = random.randint(1, SIDES_ON_DIE)
    combined = first_die + second_die
    print("Sum of rolled dice:", combined)

def main():
    first_die = 10
    print("Initial value of first_die in main():", first_die)
    for i in range(3):
        simulate_roll()
    print("Value of first_die in main() after rolls:", first_die)

if __name__ == "__main__":
    main()
