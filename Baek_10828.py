import sys

n = int(input())
b = []

for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == "push":
        b.append(int(a[1]))
    elif a[0] == "pop":
        if len(b) == 0:
            print(-1)
        else:
            print(b.pop())
    elif a[0] == "size":
        print(len(b))
    elif a[0] == "empty":
        if len(b) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "top":
        if len(b) == 0:
            print(-1)
        else:
            print(b[-1])