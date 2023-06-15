import random
from graph import hangman
from graph import logo

def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    cprint (" "+logo, "magenta")
    cprint("\n Welcome to HANGMAN game!\n\n","green")
    user_name=get_user_name()
    user_age=get_user_age(user_name)


def get_user_name():
    """
    Get a name from user and check if all are alphabetic
    """
    valid=False
    while (not valid):
        user_name=input(cprint("\n What is your name? (Just alphabetic)\n\n" ,"green"))
        if user_name.isalpha():
            user_name=user_name.capitalize()
            cprint(f"\n Happy to have you here {user_name}!\n\n", "green")
            valid=True
        else:
            cprint("\n Name contains invalid characters. Try again!\n\n", "red")
    return user_name


def get_user_age(user_name):
    """
    Get the age and check if all is digit and then ckech the eligibility
    """
   #Check if the user_age is a number
    while True:
        user_age=input(cprint("\n Pleas let me know your age? (Just insert number)\n\n", "green"))
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
    cprint(f"\n Goodbye {user}\nExit the Game\n\n", "blue")
    exit()


def rules():
    """
    This function will read the file rules.txt and
    print it in the console
    """
    try:
        with open('rules.txt') as file:
            cprint(file.read(), "green")
    except FileNotFoundError:
        cprint("\n Unable to load rules\n\n", "red")


def words():
    """
    This function will read the file words.txt and
    return it as a list
    """
    try:
        with open('words.txt') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        cprint("\n Unable to load words list\n\n", "red")


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
    #The return is added because of using it in input
    return ""

main()
