def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Handle an empty string
    if aStr == '':
        return False
    
    # Base case: Compare directly if len(aStr) = 1
    if len(aStr) == 1:
        return aStr == char
    
    # Base case: Compare char with the middle char
    middle_point = int(len(aStr)/2) 
    if aStr[middle_point] == char:
        return True
    
    # Recursive case: search on the right hand side if char > middle char
    if char > aStr[middle_point]:
        return isIn(char, aStr[middle_point+1:])
    
    # Recursive case: search on the left hand side if char < middle char
    if char < aStr[middle_point]:
        return isIn(char, aStr[:middle_point])

print(isIn("m", "abcdefg"))
print(isIn("m", "mnopqrst"))
