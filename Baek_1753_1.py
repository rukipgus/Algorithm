import sys
from collections import deque
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
a = [[] for _ in range(v+1)]
b = [sys.maxsize for _ in range(v+1)]
b[k] = 0

for i in range(e):
    x, y, w = map(int, sys.stdin.readline().split())
    a[x].append([w, y])

q = []

heapq.heappush(q, [0,k])

while q:
    print(q)
    d, n = heapq.heappop(q)
    for x, y in a[n]:
        x += d
        if x < b[y]:
            b[y] = x
            heapq.heappush(q, [x, y])

for i in range(1, v+1):
    if b[i] == sys.maxsize:
        print("INF")
    else:
        print(b[i])