import sys

n = int(sys.stdin.readline())
b = [(n-i) for i in range(n)]
a = [0]
d = []
count = 0

while True:
    c = int(sys.stdin.readline())
    if a[-1] < c:
        while True:
            if a[-1] == c:
                break
            a.append(b.pop())
            d.append("+")
    if a[-1] == c:
        a.pop()
        d.append("-")
        count += 1
    else:
        print("NO")
        exit()
    if a[-1] == 0 and len(b) == 0:
        if count == n:
            for i in range(len(d)):
                print(d[i])
            exit()
        else:
            print("NO")
            exit()