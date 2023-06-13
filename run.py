def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    user_name=get_user_name()
    #Because the input is always string in case of getting numbers should be wrap in int()
    user_age=int(input("Please let me know how old are you?"))
    if user_age>6:
        print("you are eligible to play this game")
        play_game=input("Do you want to play game (Y or N)?")
        if play_game.lower()=='y':
            #run function to start game
            pass
        else:
            #exit
            exit(user_name)
    else:
        print("you are NOT eligible to play this game")
        exit(user_name)

def get_user_name():
    """
    get a name from user and check if all are alphabetic
    """
    print("Welcome to HANGMAN game!")
    valid=False
    while (not valid):
        user_name=input("What is your name? (Just alphabetic)")
        if user_name.isalpha():
            print(f"Happy to have you here {user_name}!")
            valid=True
            return user_name
        else:
            print("The name which you inserted \nhas non-alphabetic characters.\nPlease try again!")


def exit(user):
    """
    This function will simply raise SystemExit and
    the reason of its exist is to avoid repeatation
    """
    raise SystemExit(f"\nGoodbye {user}\nExit the Game.\n")
        


main()