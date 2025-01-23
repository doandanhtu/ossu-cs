def gen_primes():
    yield 2
    prime = 2
    primes = [2]
    while True:
        prime = prime + 1
        for p in primes:
            if (prime % p) == 0:
                break
        else:
            primes.append(prime)
            yield prime

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

x = gen_primes()
y = genPrimes()

no_check = 8

for i in range(no_check):
    print(x.__next__() == y.__next__())




