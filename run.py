def main():
    """
    Getting user's name and age and starting (or restarting) and
      finishing the game 
    """
    print("Welcome to HANGMAN game!")
    user_name=input("What is your name?")
    print(f"Happy to have you here {user_name}!")
    eligible=None
    #Because the input is always string in case of getting numbers should be wrap in int()
    user_age=int(input("Please let me know how old are you?"))
    if user_age>6:
        print("you are eligible to play this game")
        Play_game=input("Do you want to play game (Y or N)?")
        if Play_game.lower()=='y':
            #run function to start game
            input("This is a test to check if we are still in the game")
        else:
            #exit
            return 0
    else:
        print("you are NOT eligible to play this game")
        return 0

main()