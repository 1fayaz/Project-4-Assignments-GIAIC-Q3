# Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

# ===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

MAX_ITEMS: int = 3

def trim_list(input_list):
    
    while len(input_list) > MAX_ITEMS:
        removed = input_list.pop()
        print(f"Removed: {removed}")

# No changes needed below this line

def collect_list():
    
    items = []
    entry = input("Enter an item (or press Enter to finish): ")
    while entry != "":
        items.append(entry)
        entry = input("Enter another item (or press Enter to finish): ")
    return items

def run():
    user_list = collect_list()
    trim_list(user_list)

if __name__ == '__main__':
    run()
