# Hangman Game

Welcome to Hangman Game, a classic word guessing game implemented in Python! This game runs in the terminal, allowing you to challenge your word-solving skills and have fun while doing it.

[View the live project here.](https://hangman-fazel.herokuapp.com//)

![Responsice Mockup](documentation/amiresponsive.jpg)

## About

Hangman Game is a classic word guessing game where players attempt to uncover a hidden word by suggesting letters or providing the full answer. In this version of the game, you'll be pitted against the computer as your opponent.

The hidden word is represented by a series of dashes, with each dash representing a letter in the word. When you suggest a letter that exists in the word, it will be revealed in all its correct positions. However, if your suggestion is incorrect, the computer will incrementally draw the hangman diagram.

The game continues until either the entire word is guessed correctly or the hangman's diagram is completed, resulting in a loss. You have a total of 7 attempts to decipher the word correctly and emerge victorious.

All the words used in this game are categorized into four categories: Countries, Animals, Foods, and Objects. 

##  User Experience (UX)

- ### UX

    -   #### As a User, I should to be able to:

        1. Acquire a clear comprehension of how to navigate the game and start playing.
        2. Conveniently obtain comprehensive guidelines for gameplay.
        3. Understand the necessary user input and receive suitable error messages to maintain game stability.
        4. Track the number of incorrect guesses until the game reaches its conclusion.
        5. Uncover the secret word if the user fails to guess it within the allotted attempts.
        6. Seamlessly proceed with the game without the requirement to reenter initial inputs.
        7. Delight in an enjoyable and fully operational gaming experience.
## Features
- ### Existing Features

    -   #### 1. Welcome Message and User Name Prompt
        - Upon launching the Hangman Game, players are greeted with a warm welcome message. They are invited to enter their name, which adds a personal touch to the gameplay experience. Here's an example of the welcome message and name prompt.
  ![Welcome](documentation/welcome.png)
  -    #### 2.User Age Prompt
        - After the player enters their name, the Hangman Game prompts them to enter their age. This feature ensures that the game is played by an appropriate age group. Players who are 6 years old or older are eligible to play the game, while those below 6 years old are considered ineligible.
        ![Age Eligibility](documentation/age.png)
  -    #### 3.Menu
        - Once the player is eligible to play the Hangman Game, they are presented with a main menu that offers three options: viewing the game rules, starting the game, or exiting the game. The main menu allows the player to choose their desired action.
        The player can enter the corresponding number to select their desired option.

             - If the player selects option 1, the game displays the rules of the Hangman Game.
             - If the player selects option 2, the game starts and the player can begin guessing the letters to uncover the secret word.
             - If the player selects option 3, the game exits gracefully with a goodbye message.

        The main menu provides an easy and intuitive way for the player to access the different functionalities of the game, allowing them to choose whether to view the rules, play the game, or exit.

        ![Menu](documentation/menu.png)
  -    ##### 3.1 Rules
        - If the player selects option 1, the game displays the rules of the Hangman Game. 
        ![Rules](documentation/rules.png)
  -    ##### 3.2 Play
        - If the player selects option 2, the game starts and the player can begin guessing the letters to uncover the secret word. 
        ![Play](documentation/play.png)
  -    ##### 3.3 Exit
        - If the player selects option 3, the game asks for confirmation before exiting. The player is prompted to enter 'Y' to confirm the exit or any other key to return to the main menu 
        ![Exit](documentation/exit.png)
-    #### 4. Category Selection
        - Once the player chooses to start the game from the main menu, they will be prompted to select a category for the secret word. The categories available for selection are "Countries," "Animals," "Foods," and "Objects."
        ![ExCategoryit](documentation/category.png)
-    #### 5. Word Guessing
        - After selecting a category, the player enters the word guessing phase of the game. The user interface will display several elements to assist the player in their guessing process.
            1. Category: The chosen category will be displayed at the top of the screen, reminding the player of the theme of the secret word.
            2. Used Letters: A list of letters that the player has already guessed will be shown. This helps the player avoid repeating guesses.
            3. Secret Word: The secret word is represented by a series of dashes, with each dash representing a letter in the word. Initially, all letters are hidden, and dashes are displayed instead. As the player correctly guesses letters, the corresponding dashes are replaced with the revealed letters.
            4. Hangman Stage: A graphical representation of the hangman will be displayed. With each incorrect guess, a new part of the hangman is added, gradually completing the figure. The stage of the hangman visually indicates the player's progress and the number of incorrect guesses made so far.

        The player will be prompted to enter a letter as their guess. If the letter is valid (a single alphabetic character that has not been previously guessed), the game will evaluate whether the letter is present in the secret word. If the guessed letter is correct, it will be revealed in the corresponding positions in the secret word. Otherwise, the hangman stage will progress, indicating an incorrect guess.

        ![Guess](documentation/guess.png)
-    #### 5. Result
        - The game continues until one of the following conditions is met:

            - The player correctly guesses the entire secret word, resulting in a victory.
            - The hangman stage is completed, indicating that the player has run out of allowed incorrect guesses, resulting in a loss.

            At the end of the game, the player will be notified of the outcome (win or loss) and shown the complete secret word.
            ![Won](documentation/won.png)
            ![Lost](documentation/lost.png)
        






