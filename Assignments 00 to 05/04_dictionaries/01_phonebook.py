# Problem Statement

# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# =========================================================================================================

def collect_contacts():
    """
    Collects names and phone numbers from the user.
    Returns a dictionary representing the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Enter a name (or press Enter to finish): ")
        if name == "":
            break
        number = input(f"Enter phone number for {name}: ")
        phonebook[name] = number

    return phonebook


def display_phonebook(phonebook):
    """
    Displays all name-number pairs in the phonebook.
    """
    print("\nPhonebook entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def search_phonebook(phonebook):
    """
    Allows the user to look up numbers by name.
    """
    print("\nPhonebook lookup:")
    while True:
        name = input("Enter a name to look up (or press Enter to stop): ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = collect_contacts()
    display_phonebook(phonebook)
    search_phonebook(phonebook)


if __name__ == '__main__':
    main()
