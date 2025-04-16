# Problem Statement
# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

# Here are two sample runs of the program, one for each return option (user input in bold italics):

# (Entered age is an adult age)

# How old is this person?: 35

# True

# (Entered age is not an adult age)

# How old is this person?: 7

# False

# ==================================================================================================================================================================================================================================================================================================================================================


ADULT_AGE: int = 18  # Legal adult age

def is_adult(age: int) -> bool:
    """
    Returns True if the age is greater than or equal to ADULT_AGE, else False.
    """
    return age >= ADULT_AGE

########## No need to edit code beyond this point :) ##########

def main():
    age = int(input("How old is this person? "))
    print(is_adult(age))

if __name__ == "__main__":
    main()
