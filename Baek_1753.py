import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
a = [[] for _ in range(v+1)]

for i in range(e):
    x, y, w = map(int, sys.stdin.readline().split())
    a[x].append([y, w])

def bfs(k):
    b = [987654321 for _ in range(v+1)]
    c = deque([[k, 0]])
    while True:
        print(c)
        t = c.popleft()

        for i in range(len(a[t[0]])):
            u = t[1] + a[t[0]][i][1]
            p = a[t[0]][i][0]
            if b[p] > u and a[p] != k:
                b[p] = u
                c.append([p, u])
        
        if len(c) == 0:
            return b

ans = bfs(k)

for i in range(1, v+1):
    if i == k:
        print(0)
    elif ans[i] == 987654321:
        print("INF")
    else:
        print(ans[i])