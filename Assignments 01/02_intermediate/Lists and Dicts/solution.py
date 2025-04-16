# Task 1: Playing with Fruits

def fruits_demo():
    basket = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Display the items in the basket
    print("Fruits in the basket:", " | ".join(basket))

    # Show how many fruits are in the basket
    print(f"Total fruits: {len(basket)}")

    # Add a new fruit
    basket.append('mango')
    print("After adding mango:", " | ".join(basket))


# Task 2: List Operations Playground

def get_item(data, pos):
    if pos >= 0 and pos < len(data):
        return data[pos]
    else:
        return "❌ That index doesn't exist."

def update_item(data, pos, value):
    if 0 <= pos < len(data):
        data[pos] = value
        return data
    else:
        return "❌ Invalid index!"

def extract_slice(data, start_idx, stop_idx):
    return data[start_idx:stop_idx]

def list_game():
    items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    while True:
        print("\n🧺 Current List:", items)
        print("Select an action:")
        print("1️⃣ View an item by index")
        print("2️⃣ Change an item")
        print("3️⃣ Slice a portion of the list")
        print("4️⃣ Quit")

        option = input("Your choice (1-4): ")

        if option == "1":
            try:
                pos = int(input("Enter the index you want to view: "))
                print("Result:", get_item(items, pos))
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif option == "2":
            try:
                pos = int(input("Enter the index to update: "))
                val = input("New value: ")
                outcome = update_item(items, pos, val)
                if isinstance(outcome, list):
                    print("✅ List updated:", outcome)
                else:
                    print("Error:", outcome)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif option == "3":
            try:
                start = int(input("Start index: "))
                end = int(input("End index: "))
                sliced = extract_slice(items, start, end)
                print("Sliced Segment:", sliced)
            except ValueError:
                print("⚠️ Please enter valid numbers.")

        elif option == "4":
            print("👋 See you next time!")
            break

        else:
            print("❗ Invalid selection, please choose from 1 to 4.")

# Run both parts
if __name__ == "__main__":
    fruits_demo()
    list_game()
