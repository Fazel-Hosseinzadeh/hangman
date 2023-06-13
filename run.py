def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    print("Welcome to HANGMAN game!")
    user_name=get_user_name()
    user_age=get_user_age(user_name)
    rules()
    
        

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
    user_age=int(input("Pleas let me know your age? (Just number)"))
    if user_age>6:
        print("you are eligible to play this game")
    else:
        print("you are NOT eligible to play this game")
        exit(user_name)
    return user_age


def exit(user):
    """
    This function will simply raise SystemExit and
    the reason of its exist is to avoid repeatation
    """
    raise SystemExit(f"\nGoodbye {user}\nExit the Game.\n")
        
def rules():
    """
    This function will read the file rules.txt and
    print it in the console
    """
    try:
        with open('rules.txt') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found or cannot be opened.")

main()