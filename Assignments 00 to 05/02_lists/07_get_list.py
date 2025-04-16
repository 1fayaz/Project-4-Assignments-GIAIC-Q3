# Problem Statement

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


# =================================================================================================================================================================================================


def collect_values():
    
    entries = []  

    user_input = input("Type something to add (or press Enter to finish): ")
    while user_input: 
        entries.append(user_input) 
        user_input = input("Add another (or press Enter to finish): ")

    print("Your final list is:", entries)


if __name__ == '__main__':
    collect_values()
