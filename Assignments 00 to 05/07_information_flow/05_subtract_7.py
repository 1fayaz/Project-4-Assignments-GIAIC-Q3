# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


def subtract_seven(number: int) -> int:
    """
    Subtracts 7 from the given number and returns the result
    """
    return number - 7

def main():
    num = 7
    result = subtract_seven(num)
    print("This should be zero:", result)

if __name__ == '__main__':
    main()
