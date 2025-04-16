# Problem Statement

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def main():
    print("Let's add two numbers!")
    
    first :int = input ("Enter the first number: ")
    second :int = input("Enter the second number: ")
    
    first = int(first)
    second = int(second)
    
    sum_of_numbers = first + second
    
    print("The result is " + str(sum_of_numbers))

    main()



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()