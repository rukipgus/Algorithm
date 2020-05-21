import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[] for i in range(n+1)]
c = [0 for i in range(n+1)]

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    a[x].append(y)
    a[y].append(x)

b = deque([1])

while True:
    t = b.popleft()
    for i in range(len(a[t])):
        if c[a[t][i]] == 0:
            c[a[t][i]] = t
            b.append(a[t][i])
    
    if len(b) == 0:
        break

for i in range(2,n+1):
    print(c[i])