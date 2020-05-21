import sys
import collections

m, n, h = map(int, sys.stdin.readline().split())
a = [[list(map(int, sys.stdin.readline().split())) for k in range(n)] for i in range(h)]
b = collections.deque([])
u = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
t = 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                b.append((j, k, i))

while b:
    c = b.popleft()

    for x,y,z in u:
        x1 = c[0] + x
        y1 = c[1] + y 
        z1 = c[2] + z
        
        if 0<= x1 <n and 0<= y1 <m and 0<= z1 <h:
            if a[z1][x1][y1] == 0:
                a[z1][x1][y1] = (a[c[2]][c[0]][c[1]] + 1)
                t = a[z1][x1][y1]
                b.append((x1, y1, z1))

for i in range(h):
    for j in range(n):
        if 0 in a[i][j]:
            print(-1)
            exit()

print(t-1)