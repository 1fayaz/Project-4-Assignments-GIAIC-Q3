# Project 4: CodeWord Cracker - A Unique Hangman 

import random

def codeword_cracker():
    tech_terms = ['typescript', 'interface', 'function', 'callback', 'variable', 'enum', 'tuples', 'asynchronous', 'promise', 'compiler']
    secret_word = random.choice(tech_terms)
    attempts_left = 7
    guessed = set()
    progress = ["_"] * len(secret_word)

    print("\n🧩 Welcome to CodeWord Cracker!")
    print("Can you reveal the tech word before your tries run out?")
    print(f"The mystery word contains {len(secret_word)} letters: {' '.join(progress)}")

    while attempts_left > 0:
        letter = input("\n🔡 Enter a letter: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("🚫 Invalid input! Please enter one letter.")
            continue

        if letter in guessed:
            print("🔁 You've already used that letter. Try something else.")
            continue

        guessed.add(letter)

        if letter in secret_word:
            print(f"🟢 Nice! '{letter}' is part of the word.")
            for index, char in enumerate(secret_word):
                if char == letter:
                    progress[index] = letter
        else:
            attempts_left -= 1
            print(f"❌ Nope! '{letter}' isn’t in the word. Tries left: {attempts_left}")

        print("📖 Current progress: " + " ".join(progress))

        if "_" not in progress:
            print(f"\n🎉 Well done! You cracked the code word: {secret_word.upper()}")
            break

    if "_" in progress:
        print(f"\n💀 Mission failed! The word was: {secret_word.upper()}")

    restart = input("\n🔁 Play again? (yes/no): ").strip().lower()
    if restart == ("yes"):
        codeword_cracker()
    else:
        print("Thanks for cracking with us! 🔐")

codeword_cracker()

print("\n🎮 Created by cool coder = ME 😎")
