# Test tuple
tup = ('I', 'am', 'a', 'test', 'tuple')

# My solution
def odd_tuples(tup):
    new_tup = ()
    for i, e in enumerate(tup):
        if i % 2 == 0:
            new_tup += (tup[i], )
    return new_tup

# Recommended sol 1
def odd_tuples2(tup):
    new_tup = ()
    i = 0
    while i < len(tup):
        new_tup += (tup[i], )
        i += 2
    return new_tup

# Recommended sol 2
def odd_tuples3(tup):
    return tup[::2]
    
# Test
print(odd_tuples(tup))
print(odd_tuples2(tup))
print(odd_tuples3(tup))