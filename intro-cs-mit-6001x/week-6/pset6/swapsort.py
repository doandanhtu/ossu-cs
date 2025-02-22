from random import randint

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
L3 = [randint(0, 9) for x in range(0, 10)]

swapSort(L1)
swapSort(L2)

modSwapSort(L1)
modSwapSort(L2)

swapSort(L3)
modSwapSort(L3)


