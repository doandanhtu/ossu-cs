def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

test_list = [1, -4, 8, -9]
test_1 = test_list[:]
test_2 = test_list[:]
test_3 = test_list[:]

# Sample
def times_five(x):
    return 5 * x

apply_to_each(test_list, times_five)
print(test_list)

#1
apply_to_each(test_1, abs)
print(test_1)

#2
def add_one(x):
    return x + 1

apply_to_each(test_2, add_one)
print(test_2)

#3
def square(x):
    return x * x

apply_to_each(test_3, square)
print(test_3)
