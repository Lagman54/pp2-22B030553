def histogram(arr):
    for i in arr:
        for j in range(i):
            print('*', end='')
        print()


histogram([4, 9, 7])
