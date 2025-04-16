import random

rounds = 5
score = 0

print("🕹️ Let's play the High-Low Challenge!")
print("=" * 60)

for current_round in range(1, rounds + 1):
    print(f"\n🎲 Round {current_round} of {rounds}")
    
    player_num = random.randint(1, 100)
    opponent_num = random.randint(1, 100)

    print(f"Your number: {player_num}")

    prediction = input("Is your number higher or lower than the computer's? (Type 'higher' or 'lower'): ").strip().lower()

    correct = (prediction == "higher" and player_num > opponent_num) or \
              (prediction == "lower" and player_num < opponent_num)

    if correct:
        print("✅ Nice one! You guessed it right.")
        print("+1 point added to your score.")
        score += 1
    else:
        print("❌ Nope, that wasn't correct.")
        if score > 0:
            score -= 1

    print(f"💻 Computer's number was: {opponent_num}")
    print(f"📊 Current Score: {score}")

print("\n" + "=" * 60)
print(f"🏁 Final Score: {score} / {rounds}")

if score == rounds:
    print("🥇 Amazing! You nailed every round! True High-Low champion!")
elif score >= rounds * 0.7:
    print("🎉 Great work! You've got a good eye for numbers!")
elif score >= rounds * 0.4:
    print("👍 Not bad! You're improving. Keep practicing!")
else:
    print("😬 Tough round! But don’t give up — try again!")

print("=" * 60)
