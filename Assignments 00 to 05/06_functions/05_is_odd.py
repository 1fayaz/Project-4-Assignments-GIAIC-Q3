# Problem Statement

# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

# =================================================================================

def is_odd(value: int) -> bool:
    """
    Returns True if the given value is odd, otherwise False.
    """
    return value % 2 == 1

def main():
    for i in range(10):
        if is_odd(i):
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

if __name__ == '__main__':
    main()
