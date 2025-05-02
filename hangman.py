#need to import random to select a random word from a list
import random

# ANSI color codes for colored terminal text
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ASCII art to show different stages of the hangman depending on how many wrong guesses the user has made
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Function to get a random word 
def get_word():
    try:
        # attempt to open and read list of words from "words.txt"
        with open("words.txt", "r") as file:
            # read lines from the file and strip whitespace, convert to lowercase
            # processed words are stored in list, words
            words = [line.strip().lower() for line in file]
        # return a random word from the list
        return random.choice(words)
    # if the file is not found, fall back to a default list of words
    except FileNotFoundError:
        return random.choice(["python", "hangman", "challenge", "code", "guess", "cold", "winter", "summer", "sunny", "rainy"])

# Function to display the current state of the game
# it shows the hangman picture, the word with guessed letters, and wrong guesses
def display_game(hangman_pics, wrong_guesses, correct_guesses, word):
    #print hangman picture based on the number of wrong guesses
    print(hangman_pics[len(wrong_guesses)])
    #print the word with guessed letters and underscores for unguessed letters
    display = [letter if letter in correct_guesses else "_" for letter in word]
    #join the letters with spaces
    print("Word: " + " ".join(display))
    #print the wrong guesses
    print("Wrong guesses: " + ", ".join(wrong_guesses))

# Function to play the game
# initializes the game, gets a word, and manages the game loop
def play_game():
    # Get a random word from the list
    word = get_word()
    # initialise correct and wrong guesses as empty lists
    correct_guesses = []
    wrong_guesses = []
    # set the number of attempts left based on the length of hang
    attempts_left = len(HANGMAN_PICS) - 1

    # print the welcome message with color and then reset text color to default
    #reset allows color to only be applied to the text that follows it
    print(CYAN + "Welcome to Hangman!" + RESET)

    #loop to keep asking for guesses until the user has either guessed the word or run out of attempts
    while len(wrong_guesses) < attempts_left:
        display_game(HANGMAN_PICS, wrong_guesses, correct_guesses, word)
        # ask the user for a letter
        # convert the input to lowercase to handle case insensitivity
        guess = input(YELLOW + "Guess a letter: "+ RESET).lower()
        # check if the input is valid (an alphabetic letter and only a single letter)
        if not guess.isalpha() or len(guess) != 1:
            print(RED + "Please enter a single letter." + RESET)
            continue
        # check if the letter has already been guessed (either correctly or incorrectly)
        if guess in correct_guesses + wrong_guesses:
            print(YELLOW + "You already guessed that letter." + RESET)
            continue

        # check if the guessed letter is in the word
        # if it is, add it to the correct guesses list
        if guess in word:
            correct_guesses.append(guess)
            print(GREEN + "Good guess!" + RESET)
        # if it is not, add it to the wrong guesses list
        else:
            wrong_guesses.append(guess)
            print(RED + "Wrong guess!" + RESET)

        # Check if the user has guessed all letters in the word
        # if so, congratulate the user and end the game
        if all(letter in correct_guesses for letter in word):
            print(GREEN + f"\nCongratulations! You guessed the word: {word}" + RESET)
            break

    # if the user has run out of attempts, display the game state and the correct word
    # and inform the user that they have lost and end the game
    else:
        display_game(HANGMAN_PICS, wrong_guesses, correct_guesses, word)
        print(RED + f"\nGame Over! The word was: {word}" + RESET)
        print(RED + "Better luck next time!" + RESET)

# helps make sure the game runs only when this script is executed directly
if __name__ == "__main__":
    while True:
        play_game()
        # ask the user if they want to play again
        play_again = input(YELLOW + "\nDo you want to play again? (yes/no): " + RESET).strip().lower()
        if play_again not in ["yes", "y"]:
            print(CYAN + "Thanks for playing! Goodbye." + RESET)
            break