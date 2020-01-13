import sys

n = int(sys.stdin.readline())

b = [1,1,1,2,2]

for i in range(n):
    c = [1,1,1,2,2]
    a = int(sys.stdin.readline())
    if a < 6:
        print(b[a-1])
    else:
        for j in range(a-5):
            t = c[0]
            c[0] = c[1]
            c[1] = c[2]
            c[2] = c[3]
            c[3] = c[4]
            c[4] = t+c[4]

        print(c[4])