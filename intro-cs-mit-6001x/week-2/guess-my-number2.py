"""
Improved version of guess my number
"""

min = 0
max = 100
print(f'Please think of a number between {min} and {max}')

# Set up loop variable
guessed = False
while not guessed:
    guess = int((min + max) / 2)
    print(f'Is your secret number {guess}?')
    ans = input("Enter 'h' to indicate the guess is too high. "
                    "Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly. ")
    
    # Progress the game if valid response
    if ans == 'l':
        min = guess
    elif ans == 'h':
        max = guess
    elif ans == 'c':
        guessed = True
    else:
        print("Sorry, I did not understand your input.")

    