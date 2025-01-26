for iteration in range(1,5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break

s = 'abcd'
print(s[2:4])
t = ''
print(len(t))