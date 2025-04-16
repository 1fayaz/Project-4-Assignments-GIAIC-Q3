# Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# =================================================================================================================================================================================================================================================================================


def display_first_item(data_list):
   
    if data_list:
        print(f"The first item is: {data_list[0]}")
    else:
        print("The list is empty. No first item to display.")

def collect_items():
    
    items = []
    user_input = input("Enter an item (or press enter to finish): ")
    while user_input != "":
        items.append(user_input)
        user_input = input("Enter another item (or press enter to finish): ")
    return items

def start_program():
    user_list = collect_items()
    display_first_item(user_list)

if __name__ == '__main__':
    start_program()
