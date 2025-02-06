def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
L2 = []
L3 = [1]
L4 = [1, 2]
L5 = [1, 2, 3]

e1 = 2
e2 = 9
e3 = 0
e4 = 4

test_lists = [L1, L2, L3, L4, L5]
test_elements = [e1, e2, e3, e4]

for L in test_lists:
    for e in test_elements:
        print(search(L, e))
        print(newsearch(L, e))
        print()
    print("next L")


