# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    chars = set(list(secretWord))
    for char in chars:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    chars = list(secretWord)
    guess = ''
    for char in chars:
        if char in lettersGuessed:
            guess += char
        else:
            guess += ' _ '
    return guess
        


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_chars = ''
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            available_chars += char
    return available_chars
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Initiate variables used to track the game state
    maximum_guesses = 8
    mistakes_made = 0
    letters_guessed = []

    # Start the game
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")
    print("-------------")

    # Run the game loop
    while maximum_guesses - mistakes_made > 0 and '_' in getGuessedWord(secretWord, letters_guessed):
        print(f"You have {maximum_guesses - mistakes_made} guesses left.")
        print(f"Available letters: {getAvailableLetters(letters_guessed)}")
        
        # Prompt the user for the guess and process it to ensure it is in lower case
        guess = input("Please guess a letter: ")
        guess = guess.lower()

        # If guess is not valid
        if guess not in getAvailableLetters(letters_guessed):
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, letters_guessed)}")
            print("-------------")
            continue
        
        # If guess is valid
        if guess in getAvailableLetters(letters_guessed):
            letters_guessed.append(guess)

            # If guess is correct
            if guess in secretWord:
                print(f"Good guess: {getGuessedWord(secretWord, letters_guessed)}")
                print("-------------")
                continue
            
            # If guess is incorrect:
            else:
                mistakes_made += 1
                print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, letters_guessed)}")
                print("-------------")
                continue

    if '_' in getGuessedWord(secretWord, letters_guessed):
        print(f"Sorry, you ran out of guesses. The word was {secretWord}.")
    else:
        print("Congratulations, you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)