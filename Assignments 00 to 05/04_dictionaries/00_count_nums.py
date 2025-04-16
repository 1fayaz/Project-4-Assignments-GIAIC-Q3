# Problem Statement

# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# =========================================================================================================================================================================================================================================================================================================================================================


def collect_numbers():
    
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        if user_input == "":
            break
        
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return numbers

def count_occurrences(numbers):
    
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

def display_counts(counts):
    
    print("\nNumber frequencies:")
    for number, count in counts.items():
        print(f"{number} appears {count} time{'s' if count > 1 else ''}.")

def main():
    user_numbers = collect_numbers()
    number_counts = count_occurrences(user_numbers)
    display_counts(number_counts)

if __name__ == '__main__':
    main()
