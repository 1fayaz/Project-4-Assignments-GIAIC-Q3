# Problem Statement

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.


# =====================================================================================================================================================================================================================

VOTING_AGE_PETURKSBOUIPO = 16
VOTING_AGE_STANLAU = 25
VOTING_AGE_MAYENGUA = 48

def main():
    age = int(input("Enter your age: "))

    if age >= VOTING_AGE_PETURKSBOUIPO:
        print(f"You are eligible to vote in Peturksbouipo (voting age: {VOTING_AGE_PETURKSBOUIPO}).")
    else:
        print(f"You are not old enough to vote in Peturksbouipo (voting age: {VOTING_AGE_PETURKSBOUIPO}).")

    if age >= VOTING_AGE_STANLAU:
        print(f"You are eligible to vote in Stanlau (voting age: {VOTING_AGE_STANLAU}).")
    else:
        print(f"You are not old enough to vote in Stanlau (voting age: {VOTING_AGE_STANLAU}).")

    if age >= VOTING_AGE_MAYENGUA:
        print(f"You are eligible to vote in Mayengua (voting age: {VOTING_AGE_MAYENGUA}).")
    else:
        print(f"You are not old enough to vote in Mayengua (voting age: {VOTING_AGE_MAYENGUA}).")

if __name__ == '__main__':
    main()
