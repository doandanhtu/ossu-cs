"""
This is an implementation of bisection search to find square root
"""

x = 23
eps = 0.01
num_guesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= eps:
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('Number of guesses: ', str(num_guesses))
print(str(ans) + ' is close to square root of ' + str(x))
