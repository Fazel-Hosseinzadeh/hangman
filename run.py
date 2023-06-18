import random
import time
from graph import hangman
from graph import logo
from graph import menu_text
from graph import play_cat
from words import categories
# Constant variable for typing()
FAST = 0.005
SLOW = 0.03
SUPPERSLOW = 0.6


def main():
    """
    Executes the main logic of the HANGMAN game.
    This function displays the game's logo, welcomes
    the user to the HANGMAN game,prompts the user to
    enter their name, retrieves the user's age,
    and displays the game menu.
    """
    cprint(logo, "magenta")
    typing("Welcome to HANGMAN game!", "blue", False, SLOW)
    user_name = get_user_name()
    get_user_age(user_name)
    menu(user_name)


def get_user_name():
    """
    Prompt the user to enter their name and validate if
    it contains only alphabetic characters.
    Returns:
        str: The validated user name with only
             alphabetic characters, capitalized.
    """
    valid = False
    while not valid:
        user_name = input(typing((
            "What is your name? (Just alphabetic characters)"
            ), "yellow", False, SLOW))
        # Refreshing screen after gettin input
        if user_name.isalpha():
            user_name = user_name.capitalize()
            typing("Happy to have you here ", "yellow", True, SLOW)
            typing(f"{user_name}!", "cyan", True, SLOW)
            # End of the line for inline elements
            print("\n")
            valid = True
        else:
            typing((
                "Name contains invalid characters. Try again!"
                ), "red", False, FAST)
    return user_name


def get_user_age(user_name):
    """
    Prompt the user to enter their age, validate if it contains only digits,
    and check eligibility.
    Args:
        user_name (str): The name of the user.
    Returns:
        str: The validated user age.
    """
    # Check if the user_age is a number
    while True:
        user_age = input(typing((
            f"How old are you {user_name}? (Just insert number)"
            ), "yellow", False, SLOW))
        if user_age.isdigit():
            break
        else:
            typing("Just numbers are valid! Try again.", "red", False, FAST)
# Check if the user_age is eligible
    if int(user_age) > 6:
        typing("you are eligible to play this game", "blue", False, SLOW)
    else:
        typing("you are NOT eligible to play this game", "red", False, FAST)
        exit_game(user_name)
    return user_age


def exit_game(user):
    """
    Exit the Hangman game and display a farewell message to the user.

    Args:
        user (str): The name of the user.

    Returns:
        None
    """

    typing((
        f" Goodbye {user}!\n We hope you enjoyed your time here.\n"
        "Exiting Hangman..."
        ), "blue", False, FAST)
    exit()


def rules():
    """
    Display the rules of the game by reading them from a file.

    Raises:
        FileNotFoundError: If the rules file 'rules.txt' is not found.

    Returns:
        None

    """
    try:
        # The "with" statement takes care of closing the file
        with open('rules.txt') as file:
            cprint(file.read(), "blue")
            # Spacing from menu
            print("\n")
    except FileNotFoundError:
        typing("Unable to load rules", "red", False, FAST)


def word_picker(category):
    """
    Pick a random word from the specified category.

    Args:
        category (int): The category index to pick the word from.

    Returns:
        str: The randomly picked word.

    """
    words = categories[category]
    return random.choice(words)


def cprint(text, color):
    """
Print colored text using ANSI escape codes for background colors.

Args:
    text (str): The text to be printed.
    color (str): The background color to be used.
                 Supported colors are 'black', 'red',
                 'green', 'yellow', 'blue', 'magenta',
                 'cyan', 'white', and 'reset'. If an invalid
                 color is provided, the text will be printed with
                 the default 'reset' color.

Returns:
    None

"""
    # ANSI escape codes for bakcground colors
    colors = {
        'black': '\033[1;40m',
        'red': '\033[1;41m',
        'green': '\033[1;42m',
        'yellow': '\033[1;33m',
        'blue': '\033[1;44m',
        'magenta': '\033[1;45m',
        'cyan': '\033[1;46m',
        'white': '\033[1;47m',
        'reset': '\033[1;0m'
    }
    if color not in colors:
        color = 'reset'  # default to reset color
    # end= "" will add nothing in the end, instead of endline
    print(f"{colors[color]}{text}{colors['reset']}", end="")


def menu(user_name):
    while True:
        cprint(menu_text, "cyan")
        # Giving space to input
        print("\n")
        choose = input(typing((
            "Please choose from the menu:"
            ), "yellow", False, SLOW))
        if not choose.isdigit():
            typing("Please enter a number between 1 to 3", "red", False, FAST)
        elif choose == '1':
            rules()
        elif choose == '2':
            play(user_name)
        elif choose == '3':
            while True:
                quit = input(typing((
                    "Press Y to exit, or any other key to continue."
                    ), "blue", False, FAST))
                if quit.lower() == 'y':
                    exit_game(user_name)
                else:
                    break
        else:
            typing("Please enter a number between 1 to 3", "red", False, FAST)


def play(user_name):
    typing((
        f"You choosed to play. Good luck {user_name}!"
        ), "yellow", False, SLOW)
    category, str_category = category_picker()
    random_word = word_picker(category)
    guess(random_word, str_category)


def category_picker():
    while True:
        str_category = ""
        cprint(play_cat, "blue")
        category = input(typing((
            "Please pick one category"
            ), "yellow", False, SLOW))
        if not category.isdigit():
            typing("please enter a number between 1 to 4", "red", False, FAST)
        elif category == '1':
            str_category = "Countries"
            break
        elif category == '2':
            str_category = " Animals"
            break
        elif category == '3':
            str_category = "Foods"
            break
        elif category == '4':
            str_category = "Objects"
            break
        else:
            typing((
                "please enter a number between 1 to 4"
                 ), "red", False, FAST)
    return int(category), str_category


def guess(random_word, category):
    stage = int(0)
    used_letters = list()
    random_word_letters = list()
    guessed_word = ["-"] * len(random_word)
    # Unpacking the random_word in random_word_letters
    for letter in random_word:
        # With .lower() we are sure all letters are lowercase
        random_word_letters.append(letter.lower())
    # Get a letter from user
    while True:
        # User Interface in the game (UI)
        cprint(f"Category: {category}", "blue")
        print("\n")
        cprint(f"Used letters: {list_to_str(used_letters)}", "blue")
        typing(list_to_str(guessed_word), "yellow", False, 0)
        cprint(hangman(stage), "magenta")
        if stage > 6:
            typing("You lost! The word is ", "red", True, SLOW)
            # Special speed for showing the random_word
            typing(f"{random_word.capitalize()}", "green", True, SUPPERSLOW)
            print("\n")
            break
        if "-" not in guessed_word:
            typing("You won! The word is ", "blue", True, SLOW)
            typing(f"{random_word.capitalize()}", "green", True, SUPPERSLOW)
            print("\n")
            break
        input_letter = input(typing((
            "\n Please insert a letter"
            ), "yellow", True, SLOW))
        # check if more than one character inserted
        if len(input_letter) > 1:
            typing("Just one letter per time. Try again!", "red", False, FAST)
        else:
            # check if character is alphabatic or not
            if not input_letter.isalpha():
                typing((
                    "Just letters are valid. Try again!"
                    ), "red", False, FAST)
            else:
                input_letter = input_letter.lower()
                if input_letter in used_letters:
                    cprint(f" {input_letter.upper()} is alredy used ", "red")
                    print("\n")
                elif input_letter in random_word_letters:
                    cprint(f" {input_letter.upper()} is in the word ", "green")
                    print("\n")
                    used_letters.append(input_letter)
                    # Updating the guessed_word
                    for i in range(len(random_word_letters)):
                        if random_word_letters[i] == input_letter:
                            guessed_word[i] = input_letter
                # If the letter is NOT in the random_word
                elif input_letter not in random_word_letters:
                    cprint((
                        f" {input_letter.upper()} is NOT in the word "
                        ), "magenta")
                    print("\n")
                    used_letters.append(input_letter)
                    stage += 1


def list_to_str(li):
    text = ""
    for letter in li:
        text += " " + letter + " "
    return text.upper()


def typing(text, color, inline=False, speed=0):
    words = text
    if not inline:
        print("\n")
    for char in words:
        time.sleep(speed)
        cprint(char, color)
    if not inline:
        print("\n")
    # For avoid to print None when it is used for input method
    return ""


main()
