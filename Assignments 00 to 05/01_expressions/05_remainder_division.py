# Problem Statement

# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

# =========================================================================================================================================================================


def divide_numbers():
    try:
        num1 = int(input("Enter the number to be divided: "))
        num2 = int(input("Enter the number to divide by: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    result = num1 // num2
    leftover = num1 % num2

    print(f"\nQuotient: {result}, Remainder: {leftover}")

if __name__ == "__main__":
    divide_numbers()

