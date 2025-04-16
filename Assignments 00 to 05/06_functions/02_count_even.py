# Problem Statement
# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!


# ====================================================================================================================================================================================


def count_even(numbers):
    """
    Returns the number of even integers in the given list.

    Examples:
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

def get_list_of_ints():
   
    numbers = []
    user_input = input("Enter an integer (or press Enter to finish): ")
    
    while user_input != "":
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")
        user_input = input("Enter another integer (or press Enter to finish): ")

    return numbers

def main():
    user_numbers = get_list_of_ints()
    even_count = count_even(user_numbers)
    print(f"\nYou entered {even_count} even number(s).")

if __name__ == '__main__':
    main()
