animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(a_dict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    max_length = max(map(len, a_dict.values()))
    for key in a_dict.keys():
        if len(a_dict[key]) == max_length:
            return key

# More efficient sol
def biggest1(a_dict):
    result = None
    max_length = 0
    for key in a_dict.keys():
        
        # This will result the first key with max length, change ">" to ">=" for the last one
        if len(a_dict[key]) > max_length:
            result = key
            max_length = len(a_dict[key])
    
    return result

print(biggest(animals))
print(biggest1(animals))