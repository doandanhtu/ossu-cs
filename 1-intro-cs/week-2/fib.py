from sys import argv, exit

def main():
    if len(argv) != 2:
        print('Usage: python fib.py integer')
        exit(1)

    if int(argv[1]) < 0:
        print('The supplied integer must be non-negative')
        exit(1)
  
    print(fib(int(argv[1])))
    exit(0)

def fib(x):
    """
    returns the xth Fibonacci number
    """
    if x == 0 or x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)

main()


