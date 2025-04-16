# Problem Statement

# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):

# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']

# (Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)

# ================================================================================================================================================================================================================================================================================================================================


def repeat_and_add(target_list, item):
    """Add three copies of an item to the provided list."""
    for _ in range(3):
        target_list.append(item)

def run_program():
    user_input = input("Type something to duplicate: ")
    items = []

    print("Initial list:", items)
    repeat_and_add(items, user_input)
    print("Updated list:", items)

if __name__ == "__main__":
    run_program()