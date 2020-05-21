import collections
import sys

m,n = map(int, sys.stdin.readline().split())

a = [input().split() for i in range(n)]
b = collections.deque([])
h = [(1,0),(-1,0),(0,1),(0,-1)]
count = 0
an = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == "1":
            b.append((i,j))

b.append("!")

while b:
    d = b.popleft()

    if d == "!":
        if len(b) == 0:
            break

        else:
            an += 1
            d = b.popleft()
            b.append("!")

    for x, y in h:
        x1 = d[0] + x
        y1 = d[1] + y

        if 0 <= x1 < n and 0 <= y1 < m:
            if a[x1][y1] == "0":
                a[x1][y1] = "1"
                b.append((x1, y1))

for i in range(n):
    for j in range(m):
        if a[i][j] == "0":
            print(-1)
            exit()
print(an)