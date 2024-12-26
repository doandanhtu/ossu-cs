animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# My Sol
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    return sum(map(len, animals.values()))

# Iterate over values
def how_many1(a_dict):
    result = 0
    for value in a_dict.values():
        result += len(value)
    return result

# Iterate over keys
def how_many2(a_dict):
    result = 0
    for key in a_dict.keys():
        result += len(a_dict[key])
    return result

print(how_many(animals))
print(how_many1(animals))
print(how_many2(animals))