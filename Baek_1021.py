import sys
import collections

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = [i for i in range(1, n+1)]
c = 0

for i in a:
    d = b.index(i)
    if (d) <= (len(b) - d):
        for j in range(d):
            b.append(b[0])
            del b[0]
            c += 1
    else:
        for j in range(len(b) - d):
            b.insert(0, b[-1])
            del b[-1]
            c += 1
    del b[0]

print(c)