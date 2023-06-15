import random
from graph import *
from words import *

def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    cprint (" "+logo, "magenta")
    cprint("\n Welcome to HANGMAN game!\n\n","green")
    user_name = get_user_name()
    user_age = get_user_age(user_name)
    menu(user_name)


def get_user_name():
    """
    Get a name from user and check if all are alphabetic
    """
    valid = False
    while (not valid):
        user_name = input(cprint("\n What is your name? (Just alphabetic)\n\n" ,"green"))
        if user_name.isalpha():
            user_name = user_name.capitalize()
            cprint(f"\n Happy to have you here {user_name}!\n\n", "green")
            valid = True
        else:
            cprint("\n Name contains invalid characters. Try again!\n\n", "red")
    return user_name


def get_user_age(user_name):
    """
    Get the age and check if all is digit and then ckech the eligibility
    """
   #Check if the user_age is a number
    while True:
        user_age=input(cprint(f"\n How old are you {user_name}? (Just insert number)\n\n", "green"))
        if user_age.isdigit():
            break
        else:
            cprint("\n Just numbers are valid! Try again.\n\n", "red")
    
# Check if the user_age is eligible
    if int(user_age) > 6:
        cprint("\n you are eligible to play this game\n\n", "green")
    else:
        cprint("\n you are NOT eligible to play this game\n\n", "red")
        exit_game(user_name)
    return user_age


def exit_game(user):
    """
    This function will simply raise SystemExit and
    the reason of its exist is to avoid repeatation
    """
    cprint(f"\n Goodbye {user}! We hope you enjoyed your time with us.\n Exiting Hangman...\n\n", "blue")
    exit()


def rules():
    """
    This function will read the file rules.txt and
    print it in the console
    """
    try:
        with open('rules.txt') as file:
            cprint(file.read(), "blue")
    except FileNotFoundError:
        cprint("\n Unable to load rules\n\n", "red")


def word_picker(category):
    words = categories[category]
    return random.choice(words)


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
    #The return is added because of using it in input
    return ""


def menu(user_name):
    while True:
        cprint(menu_text, "cyan")
        choose =input(cprint("\n Please choose from the menue:\n\n", "green"))
        if not choose.isdigit():
            cprint("\n\n Please enter a number between 1 to 3\n\n", "red")
        elif choose == '1':
            rules()
        elif choose == '2':
            play(user_name)
        elif choose == '3':
            while True:
                q=input(cprint(f"\n\n Press Y to quit, or any other key to continue.\n\n", "blue"))
                if q.lower()=='y':
                    exit_game(user_name)
                else:
                    break
        else:
            cprint("\n\n Please enter a number between 1 to 3\n\n", "red")


def play(user_name):
    cprint(f"\n You choosed to play. Good luck {user_name}!\n", "green")
    category = category_picker()
    random_word = word_picker(category)
    

def category_picker():
    
    while True:
        cprint(play_cat, "green")
        category = input (cprint(" Please pick one category 4 ", "green"))
        if not category.isdigit():
            cprint("\n please enter a number between 1 to 4\n", "red")
        elif category == '1':
            cprint("\n Category: Contries\n", "blue")
            break
        elif category == '2':
            cprint("\n Category: Animals\n", "blue")
            break
        elif category == '3':
            cprint("\n Category: Foods\n", "blue")
            break
        elif category == '4':
            cprint("\n Category: Things\n", "blue")
            break
        else:
            cprint("\n please enter a number between 1 to 4\n", "red")
    return int(category)


main()
