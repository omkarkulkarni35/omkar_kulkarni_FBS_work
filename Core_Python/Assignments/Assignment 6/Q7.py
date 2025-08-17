for i in range(1, 10, 2):

    for j in range(1,10-i):
        print('',end=' ')

    for j in range(1, i + 1):
        print(chr(64+j), end= ' ')

    for j in range(i):
        print(' ',end=' ')
    print()