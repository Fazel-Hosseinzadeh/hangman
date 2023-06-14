import random
from graph import hangman
from graph import logo

def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    cprint (logo, "magenta")
    print("\nWelcome to HANGMAN game!\n")
    user_name=get_user_name()
    user_age=get_user_age(user_name)


def get_user_name():
    """
    Get a name from user and check if all are alphabetic
    """
    valid=False
    while (not valid):
        user_name=input("What is your name? (Just alphabetic)")
        if user_name.isalpha():
            user_name=user_name.capitalize()
            print(f"\nHappy to have you here {user_name}!\n")
            valid=True
        else:
            print("\nThe name which you inserted \nhas non-alphabetic characters.\nPlease try again!\n")
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
        print("\nUnable to load rules\n")


def words():
    """
    This function will read the file words.txt and
    return it as a list
    """
    try:
        with open('words.txt') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("\nUnable to load words list\n")


def random_picker(ls):
    """
    This function simply will pick from the list of the 
    words which are comming from words() function
    """
    return random.choice(ls)


def cprint(text, color):

    #ANSI escape codes for bakcground colors
    colors = {
        'black': '\033[1;40m',
        'red': '\033[1;41m',
        'green': '\033[1;42m',
        'yellow': '\033[1;43m',
        'blue': '\033[1;44m',
        'magenta': '\033[1;45m',
        'cyan': '\033[1;46m',
        'white': '\033[1;47m',
        'reset': '\033[1;0m'
    }

    if color not in colors:
        color = 'reset'  # default to reset color

    print(f"{colors[color]}{text}{colors['reset']}")

main()
