import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = list(sys.stdin.readline())
    b = 0
    c = 0

    for j in a[:-1]:
        if j == "(":
            b += 1
        else:
            b -= 1
        if b < 0:
            print("NO")
            break
        c += 1
    if c == (len(a)-1):
        if b == 0:
            print("YES")
        else:
            print("NO")