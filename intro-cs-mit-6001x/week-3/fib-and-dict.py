import time

# The simple but inefficient version of fib
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2)


# Improve the efficiency using a dictionary
def fib_efficient(n, d = {1: 1, 2: 2}):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        d[n] = ans
        return ans
    
n  = 1000

fib_start_time = time.time()
#print("Executing fib...")
#print(fib(n))
fib_end_time = time.time()
#print(f"Normal fib executed successfully in {round(fib_end_time - fib_start_time, 6)} seconds") 

print("")

eff_fib_start_time = time.time()
print("Executing efficient fib...")
print(fib_efficient(n))
eff_fib_end_time = time.time()
print(f"Efficient fib executed successfully in {round(eff_fib_end_time - eff_fib_start_time, 6)} seconds") 