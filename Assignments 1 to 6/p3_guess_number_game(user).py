# Project 3: The Number Hunter Game (User Guess)

import random

def number_hunter():
    print("\n🔍 Welcome to 'The Number Hunter'!")
    print("Your mission: Find the hidden number between 1 and 100.")
    
    target = random.randint(1, 100)
    chances = 3

    while chances > 0:
        try:
            print(f"\n🔢 Attempts remaining: {chances}")
            player_guess = int(input("Take a shot: "))

            if player_guess < 1 or player_guess > 100:
                print("🚫 That number's out of bounds. Stick to 1–100!")
                continue

            if player_guess == target:
                print("🎯 Bullseye! You found the hidden number!")
                break
            elif player_guess < target:
                print("📉 Too low... the number is higher.")
            else:
                print("📈 Too high... aim lower next time.")

            chances -= 1

            if chances == 0:
                print(f"\n💥 Mission Failed! The number was {target}.")

        except ValueError:
            print("⚠️ Numbers only, please!")

    retry = input("\n🔁 Want to play again? (yes/no): ").strip().lower()
    if retry == 'yes':
        number_hunter()
    else:
        print("👋 Thanks for playing Number Hunter!")

# Launch the game
number_hunter()

print("\n🎮 Created by cool coder = ME 😎")
