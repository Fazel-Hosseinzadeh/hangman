import random
from graph import *
from words import *
import sys
import time

# Constant variable for typing()
FAST=0.001
SLOW=0.03

def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    cprint (logo, "magenta")
    typing("Welcome to HANGMAN game!","blue",False,SLOW)
    user_name = get_user_name()
    user_age = get_user_age(user_name)
    menu(user_name)


def get_user_name():
    """
    Get a name from user and check if all are alphabetic
    """
    valid = False
    while (not valid):
        user_name = input(typing("What is your name? (Just alphabetic characters)" ,"yellow", False, SLOW))
        if user_name.isalpha():
            user_name = user_name.capitalize()
            typing(f"Happy to have you here ", "yellow", True, SLOW)
            typing(f"{user_name}!", "cyan", True, SLOW)
            # End of the line for inline elements
            print("\n")
            valid = True
        else:
            typing("Name contains invalid characters. Try again!", "red", False, FAST)
    return user_name


def get_user_age(user_name):
    """
    Get the age and check if all is digit and then ckech the eligibility
    """
   #Check if the user_age is a number
    while True:
        user_age=input(typing(f"How old are you {user_name}? (Just insert number)", "yellow", False, SLOW))
        if user_age.isdigit():
            break
        else:
            typing("Just numbers are valid! Try again.", "red",False, FAST)
    
# Check if the user_age is eligible
    if int(user_age) > 6:
        typing("you are eligible to play this game", "blue",False, SLOW)
    else:
        typing("you are NOT eligible to play this game", "red",False, FAST)
        exit_game(user_name)
    return user_age


def exit_game(user):
    """
    This function will simply raise SystemExit and
    the reason of its exist is to avoid repeatation
    """
    typing(f" Goodbye {user}!\n We hope you enjoyed your time here.\n Exiting Hangman...", "blue",False, FAST)
    exit()


def rules():
    """
    This function will read the file rules.txt and
    print it in the console
    """
    try:
        with open('rules.txt') as file:
            cprint(file.read(), "blue")
            # Spacing from menu
            print("\n")
    except FileNotFoundError:
        typing("Unable to load rules", "red", False, FAST)


def word_picker(category):
    words = categories[category]
    return random.choice(words)


def cprint(text, color):

    #ANSI escape codes for bakcground colors
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
        choose =input(typing("Please choose from the menue:", "yellow", False, SLOW))
        if not choose.isdigit():
            typing("Please enter a number between 1 to 3", "red" ,False, FAST)
        elif choose == '1':
            rules()
        elif choose == '2':
            play(user_name)
        elif choose == '3':
            while True:
                q=input(typing(f"Press Y to exit, or any other key to continue.","blue",False, FAST))
                if q.lower()=='y':
                    exit_game(user_name)
                else:
                    break
        else:
            typing("Please enter a number between 1 to 3", "red",False, FAST)


def play(user_name):
    cprint(f"You choosed to play. Good luck {user_name}!", "yellow")
    category, str_category = category_picker()
    random_word = word_picker(category)
    guess(random_word,str_category)
        

def category_picker():
    
    while True:
        str_category=""
        cprint(play_cat, "blue")
        category = input (cprint("Please pick one category", "yellow"))
        if not category.isdigit():
            cprint("please enter a number between 1 to 4", "red")
        elif category == '1':
            str_category="Countries"
            break
        elif category == '2':
            str_category=" Animals"
            break
        elif category == '3':
            str_category="Foods"
            break
        elif category == '4':
            str_category="Objects"
            break
        else:
            cprint("please enter a number between 1 to 4", "red")
    return int(category), str_category


def guess(random_word, category):
    stage=int(0)
    used_letters=list()
    random_word_letters = list()
    guessed_word=["-"]* len(random_word)
    
    # Unpacking the random_word in random_word_letters
    for letter in random_word:
        # With .lower() we are sure all letters are lowercase
        random_word_letters.append(letter.lower())
    
    # Get a letter from user
    while True:
        #  User Interface in the game

        cprint( hangman(stage), "blue")

        cprint( f"Category: {category}", "blue")
        cprint( f"  ", "black")
        cprint(f"Try: {stage} of 7" , "blue")
        print("\n")

        cprint( f"Used letters: {list_to_str(used_letters)}", "blue")
        print("\n")
        cprint(list_to_str(guessed_word), "yellow") 

        if stage > 6 :
            cprint(f"You lost! The word is ", "red")
            cprint(f"{random_word.capitalize()}", "green")
            print("\n")
            break
        if "-" not in guessed_word:
            cprint(f"You won! The word is ", "green")
            cprint(f"{random_word.capitalize()}", "blue")
            print("\n")
            break

        input_letter= input(cprint("Please insert a letter", "yellow"))

        # check if more than one character inserted
        if len(input_letter)>1:
            cprint("Just one letter per time. Try again!", "red")
        else:
            # check if character is alphabatic or not
            if not input_letter.isalpha():
                cprint("Just letters are valid. Try again!", "red")
            else:
                """
                We are sure input_letter is letter,so we can use .lower() 
                method to convert it to lowercase
                """
                input_letter=input_letter.lower()
                if input_letter in used_letters:
                    cprint(f"{input_letter} is alredy used", "red")
                # If the letter is in the random_word_letters 
                elif input_letter in random_word_letters:
                    cprint(f"{input_letter} is in the word", "magenta")
                    used_letters.append(input_letter)
                    # Updating the guessed_word
                    for i in range(len(random_word_letters)):
                        if random_word_letters[i]==input_letter:
                            guessed_word[i]=input_letter
                            
                # If the letter is NOT in the random_word
                elif input_letter not in random_word_letters:
                    cprint(f"{input_letter} is NOT in the word", "cyan")
                    used_letters.append(input_letter)
                    stage += 1


def list_to_str(li):
    str=""
    for l in li:
        str +=  " " + l + " "
    return str.upper() 


def typing(str,color,inline=False,speed=0):
    words = str

    if not inline:
        print("\n")
    for char in words:
        time.sleep(speed)
        cprint(char,color)

    if not inline:
        print("\n")
    # For avoid to print None when it is used for input method
    return ""


main()
