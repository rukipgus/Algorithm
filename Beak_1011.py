import sys

a = int(input())
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    d = c-b
    e = 1
    
    while True:
        if d <= e*(e+1):
            f = d-e*(e-1)
            if f <= e:
                print(2*e-1)
                break
            else:
                print(2*e)
                break
        e+=1