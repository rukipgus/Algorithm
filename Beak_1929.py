import sys

while True:
    d = int(sys.stdin.readline())
    
    if d == 0:
        exit()
    
    c = [False,False]+[True for i in range(2, 2*d+1)]

    for i in range(2, 2*d+1):
        for j in range(2*i, 2*d+1, i):
            if c[j] == False:
                continue
            else:
                c[j] = False

    print(sum(1 for i in range(d, 2*d+1) if c[i] == True ))