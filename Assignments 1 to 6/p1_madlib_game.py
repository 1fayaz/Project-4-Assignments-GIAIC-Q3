# Project 1: Word Puzzle Riddle Game 

def word_riddle_game():
    print(" Welcome to the Word Puzzle Riddle Game!")
    print("Let's fill in some words and see what kind of riddle you solve!")

    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")

   
    print("\n🔍 Here's your riddle... Can you solve it?")
    riddle = f'''
    I am a {adjective} {noun}, found not in {place}, but inside your {noun2}.
    I can {verb} when you {verb2}, yet I make no sound.
    What am I?
    '''

    print(riddle)
    print("🤔 Think about it... but really, it's just for fun with your own words!")


word_riddle_game()

print("\n🎮 Created by cool coder = ME 😎")

