# Project 5:- A Countdown Challenge

import time
import sys

def launch_countdown(total_seconds):
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        display = f"{minutes:02d}:{seconds:02d}"
        sys.stdout.write(f"\r🕒 Countdown Running: {display} ")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1

    print("\n🚀 00:00 - Time's up! SpaceShip Lauched!")


print("🚨 Welcome to Time Blaster!")

try:
    user_time = int(input("⏰ How many seconds to count down?: "))
    launch_countdown(user_time)
except ValueError:
    print("❌ Oops! That wasn't a number. Please enter a valid time.")

print("\n🎮 Created by cool coder = ME 😎")
