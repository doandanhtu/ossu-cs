"""
A string is palindrome if it can be read the same forward and backward.
This program checks if a given string is palindrome or not.
"""

def main():
    # Prompt a string input from the user
    s = input('Enter a string: ')
    if palindrome(to_chars(s)):
        print('Your string is palindrome')
    else:
        print('Your string is not palindrome')


def palindrome(s):
    """
    Check if the string is palindrome using recursion
    """
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])
    

def to_chars(s):
    """
    Remove all non alphabetical characters from a string
    """
    s = s.lower()
    ans = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
    return ans


main()


