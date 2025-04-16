# 🔑 Project 7: Ultimate Password Maker

import random
import string
import time

def create_password(size=12):
    charset = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(charset) for _ in range(size))

def animate_loading(message="🔄 Crafting your password"):
    print(message, end="", flush=True)
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

# Start of the tool
print("🛡️ Welcome to KeyForge – Your Personal Password Crafter!")

try:
    desired_length = int(input("🔢 Enter password length (minimum 6): "))
    
    if desired_length < 6:
        print("⚠️ Oops! Minimum length should be 6 characters.")
    else:
        animate_loading()
        final_password = create_password(desired_length)
        print("✅ Your unique password is:", final_password)

except ValueError:
    print("❌ That's not a number! Please enter a valid length.")

print("\n🎮 Created by cool coder = ME 😎")
