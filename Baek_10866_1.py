import sys

n = int(sys.stdin.readline())
b = []

for i in range(n):
    a = list(sys.stdin.readline().split())

    if a[0] == "push_front":
        b.insert(0, int(a[1]))

    elif a[0] == "push_back":
        b.append(int(a[1]))

    elif a[0] == "pop_front":
        if len(b) == 0:
            print(-1)
        else:
            print(b[0])
            del b[0]
    elif a[0] == "pop_back":
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
    elif a[0] == "front":
        if len(b) == 0:
            print(-1)
        else:
            print(b[0])
    elif a[0] == "back":
        if len(b) == 0:
            print(-1)
        else:
            print(b[-1])