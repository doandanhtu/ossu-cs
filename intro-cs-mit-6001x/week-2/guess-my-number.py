"""
Implement a guess game using bisection search
"""

min = 0
max = 100
print(f'Please think of a number between {min} and {max}')

# Set up loop variable
ans = 'start'
guess = int((min + max) / 2)
while ans != 'c':

    # Get the response from user
    ans_check = True
    while ans_check:
        print(f'Is your secret number {guess}?')
        ans = input("Enter 'h' to indicate the guess is too high. "
                    "Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly. ")
        if ans == 'h' or ans == 'l' or ans == 'c':
            ans_check = False
        else:
            print("Sorry, I did not understand your input.")
    
    # Progress the game if valid response
    if ans == 'l':
        min = guess
    elif ans == 'h':
        max = guess
    elif ans == 'c':
        break
    guess = int((min + max) / 2)