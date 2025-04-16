# Problem Statement


# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# ===============================================================================================================================================================================================================================


def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    # Access the last item using its index: length of the list - 1
    print(lst[len(lst) - 1])

    # Alternatively, this shorthand also works:
    # print(lst[-1])


# No need to modify the code below this line

def get_lst():
    """
    Prompts the user to enter elements one at a time and returns the resulting list.
    Input ends when the user presses Enter without typing anything.
    """
    lst = []
    elem = input("Enter an element (or press Enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter another element (or press Enter to stop): ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()
