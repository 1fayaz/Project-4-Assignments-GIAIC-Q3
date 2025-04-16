#  Project 2: Mystery Number Challenge (Computer)

import random

def mystery_number_game():
    print("\n🔢 Welcome to the Mystery Number Challenge!")
    print("I've picked a secret number between 1 and 100.")
    print("Can you figure it out in just 3 tries?\n")

    secret = random.randint(1, 100)
    attempts = 3

    while attempts > 0:
        try:
            user_input = int(input("🔍 Your guess: "))

            if not 1 <= user_input <= 100:
                print("🚫 Only numbers between 1 and 100 are allowed.\n")
                continue

            if user_input == secret:
                print("🏆 Nailed it! You guessed the secret number!")
                break
            elif user_input < secret:
                print("📉 Hint: Try a higher number.")
            else:
                print("📈 Hint: Try a lower number.")

            attempts -= 1

            if attempts:
                print(f"🕒 Tries remaining: {attempts}\n")
            else:
                print(f"\n💀 Out of tries! The number was {secret}. Better luck next time!")

        except ValueError:
            print("⚠️ Please type a valid number!\n")


mystery_number_game()

print("\n Game created by a cool coder = ME 😎 \n")
