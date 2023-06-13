import random

def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    print("Welcome to HANGMAN game!")
    user_name=get_user_name()
    user_age=get_user_age(user_name)
    rules()
    print(words()) 
    print(random_picker(words()))
    

def get_user_name():
    """
    Get a name from user and check if all are alphabetic
    """
    valid=False
    while (not valid):
        user_name=input("What is your name? (Just alphabetic)")
        if user_name.isalpha():
            print(f"Happy to have you here {user_name}!")
            valid=True
        else:
            print("The name which you inserted \nhas non-alphabetic characters.\nPlease try again!")
    return user_name


def get_user_age(user_name):
    """
    Get the age and check if all is digit and then ckech the eligibility
    """
   #Check if the user_age is a number
    while True:
        user_age=input("Pleas let me know your age? (Just insert number)")
        if user_age.isdigit():
            break
        else:
            print("Just numbers are valid!\nPlease try again.\n")
    
# Check if the user_age is eligible
    if int(user_age) > 6:
        print("you are eligible to play this game")
    else:
        print("you are NOT eligible to play this game")
        exit_game(user_name)
    return user_age


def exit_game(user):
    """
    This function will simply raise SystemExit and
    the reason of its exist is to avoid repeatation
    """
    print(f"\nGoodbye {user}\nExit the Game.\n")
    exit()


def rules():
    """
    This function will read the file rules.txt and
    print it in the console
    """
    try:
        with open('rules.txt') as file:
            print(file.read())
    except FileNotFoundError:
        print("Unable to load rules")


def words():
    """
    This function will read the file words.txt and
    return it as a list
    """
    try:
        with open('words.txt') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Unable to load words list")


def random_picker(list):
    """
    This function simply will pick from the list of the 
    words which are comming from words() function
    """
    return random.choice(list)


main()