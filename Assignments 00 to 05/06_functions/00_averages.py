# Problem Statement

# Write a function that takes two numbers and finds the average between the two.


# ====================================================================================

def average(a: float, b: float) -> float:
    """
    Returns the number halfway between a and b.
    """
    return (a + b) / 2

def main():
    avg_one = average(0, 10)
    avg_two = average(8, 10)
    final_avg = average(avg_one, avg_two)

    print(f"Average of 0 and 10: {avg_one}")
    print(f"Average of 8 and 10: {avg_two}")
    print(f"Average of both averages: {final_avg}")

if __name__ == '__main__':
    main()
