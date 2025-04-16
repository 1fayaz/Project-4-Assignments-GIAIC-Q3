# Project 4: Battle of Hands - Rock vs Paper vs Scissors

import random

def start_battle():
    player_score = 0
    ai_score = 0
    choices = ["rock", "paper", "scissors"]

    print("\n🕹️ Welcome to Battle of Hands!")
    print("Choose your move: Rock, Paper, or Scissors.")
    print("Type 'q' anytime to end the match.\n")

    while True:
        user_input = input("▶️ Your move: ").strip().lower()

        if user_input == 'q':
            print("\n🛑 Match ended.")
            print(f"📈 Final Tally - You: {player_score} | AI: {ai_score}")
            break

        if user_input not in choices:
            print("⚠️ Invalid move! Choose Rock, Paper, or Scissors only.\n")
            continue

        ai_move = random.choice(choices)

        print(f"\n🙋 You played: {user_input}")
        print(f"🤖 AI played: {ai_move}\n")

        if user_input == ai_move:
            print("🤝 Draw! Nobody scores.")
        elif (user_input == "rock" and ai_move == "scissors") or \
             (user_input == "paper" and ai_move == "rock") or \
             (user_input == "scissors" and ai_move == "paper"):
            print("🎯 You strike a win!")
            player_score += 1
        else:
            print("💥 AI takes this round!")
            ai_score += 1

        print(f"📊 Current Score — You: {player_score}, AI: {ai_score}\n")

# Start the battle
start_battle()

print("\n🎮 Created by cool coder = ME 😎")



