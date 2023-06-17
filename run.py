import random
from graph import *
from words import *

def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    cprint (logo, "magenta")
    cprint("Welcome to HANGMAN game!","blue")
    user_name = get_user_name()
    user_age = get_user_age(user_name)
    menu(user_name)


def get_user_name():
    """
    Get a name from user and check if all are alphabetic
    """
    valid = False
    while (not valid):
        user_name = input(cprint("What is your name? (Just alphabetic characters)" ,"yellow"))
        if user_name.isalpha():
            user_name = user_name.capitalize()
            cprint(f"Happy to have you here {user_name}!", "yellow")
            valid = True
        else:
            cprint("Name contains invalid characters. Try again!", "red")
    return user_name


def get_user_age(user_name):
    """
    Get the age and check if all is digit and then ckech the eligibility
    """
   #Check if the user_age is a number
    while True:
        user_age=input(cprint(f"How old are you {user_name}? (Just insert number)", "yellow"))
        if user_age.isdigit():
            break
        else:
            cprint("Just numbers are valid! Try again.", "red")
    
# Check if the user_age is eligible
    if int(user_age) > 6:
        cprint("you are eligible to play this game", "blue")
    else:
        cprint("you are NOT eligible to play this game", "red")
        exit_game(user_name)
    return user_age


def exit_game(user):
    """
    This function will simply raise SystemExit and
    the reason of its exist is to avoid repeatation
    """
    cprint(f"Goodbye {user}! We hope you enjoyed your time with us.\n Exiting Hangman...", "blue")
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
        cprint("Unable to load rules", "red")


def word_picker(category):
    words = categories[category]
    return random.choice(words)


def cprint(text, color,inline=False):

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

    if inline==True:
        # end= " " will add space in the end instead of end line
        print(f"{colors[color]} {text} {colors['reset']}", end=" ")
    else:
        print(f"{colors[color]}\n\n  {text}  \n\n{colors['reset']}")
        #The return is added because of using it in input
        return ""


def menu(user_name):
    while True:
        cprint(menu_text, "cyan")
        choose =input(cprint("Please choose from the menue:", "yellow"))
        if not choose.isdigit():
            cprint("Please enter a number between 1 to 3", "red")
        elif choose == '1':
            rules()
        elif choose == '2':
            play(user_name)
        elif choose == '3':
            while True:
                q=input(cprint(f"Press Y to quit, or any other key to continue.","blue"))
                if q.lower()=='y':
                    exit_game(user_name)
                else:
                    break
        else:
            cprint("Please enter a number between 1 to 3", "red")


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

        cprint( f"Category: {category}", "blue", True)
        cprint( f"  ", "black", True)
        cprint(f"Try: {stage} of 7" , "blue", True)
        print("\n")

        
        cprint(list_to_str(guessed_word), "yellow", True)
        cprint( f"Used letters: {list_to_str(used_letters)}", "blue", True) 
        print("\n")

        if stage > 6 :
            cprint(f"You lost! The word is ", "red", True)
            cprint(f"{random_word.capitalize()}", "green", True)
            break
        if "-" not in guessed_word:
            cprint(f"You won! The word is ", "green", True)
            cprint(f"{random_word.capitalize()}", "blue", True)
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
                    cprint(f"{input_letter} is alredy used", "blue")
                # If the letter is in the random_word_letters 
                elif input_letter in random_word_letters:
                    cprint(f"{input_letter} is in the word", "blue")
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

main()
