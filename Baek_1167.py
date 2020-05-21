import sys
from collections import deque

n = int(sys.stdin.readline())
a = [[] for i in range(n+1)]

for i in range(n-1):
    x, y, w = map(int, sys.stdin.readline().split())
    a[x].append([y, w])
    a[y].append([x, w])

def bfs(x,n):
    b = [0 for i in range(n+1)]
    c = deque([[x, 0]])

    while True:
        #print("c:", c)
        #print("b:", b)
        t = c.popleft()

        for i in range(len(a[t[0]])):
            if b[a[t[0]][i][0]] == 0 and a[t[0]][i][0] != x:
                b[a[t[0]][i][0]] = a[t[0]][i][1] + t[1]
                c.append([a[t[0]][i][0], b[a[t[0]][i][0]]])
            
        if len(c) == 0:
            return b.index(max(b)), max(b)

ma, _ = bfs(1,n)

ans, anm = bfs(ma,n)

print(anm)