def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = min(a, b)
    while gcd > 1:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return gcd

print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))