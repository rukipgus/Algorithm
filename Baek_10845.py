import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    b = list(sys.stdin.readline().split())

    if b[0] == "push":
        a.append(int(b[1]))

    elif b[0] == "back":
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])  

    elif b[0] == "front":
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])

    elif b[0] == "pop":
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
            del a[0]

    elif b[0] == "size":
        print(len(a))

    elif b[0] == "empty":
        if len(a) == 0:
            print(1)
        else:
            print(0)