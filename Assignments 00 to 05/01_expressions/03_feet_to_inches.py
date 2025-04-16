# Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# -------------------------------------------------------------------------------------------------------------------------------------------------------



FOOT_TO_INCH = 12  

def convert_feet_to_inches():
    try:
        user_input = float(input("How many feet do you want to convert? "))
    except ValueError:
        print("Oops! Please enter a valid number.")
        return

    total_inches = user_input * FOOT_TO_INCH
    print(f"Equivalent length: {total_inches} inches")

if __name__ == "__main__":
    convert_feet_to_inches()
