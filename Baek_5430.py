import sys
import collections

t = int(input())

for i in range(t):
    f = sys.stdin.readline().split()
    n = int(sys.stdin.readline())
    a = collections.deque(list(map(int, sys.stdin.readline().replace("[","").replace("]","").replace(",", " ").split())))
    d = 0
    u = 0

    for j in f[0]:
        if j == "R":
            d += 1
        else:
            if len(a) == 0:
                u += 1
                break
            else:
                if d % 2 == 0:
                    a.popleft()
                else:
                    a.pop()

    if len(a) == 0 and u == 1:
        print("error")
    else:
        e = len(a)
        print("[", end = "")

        if e != 0:
            if d % 2 == 0:
                for j in range(e-1):
                    print(a.popleft(), end = ",")
            else:
                for j in range(e-1):
                    print(a.pop(), end = ",")
            print(a[-1], end = "")
        print("]")