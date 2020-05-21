import sys
import collections

n, m = map(int, sys.stdin.readline().split())
a = [sys.stdin.readline().rstrip() for i in range(n)]
b = [[[0,0] for j in range(m)] for i in range(n)]
h = [(1,0), (-1,0), (0,1), (0,-1)]
c = collections.deque([(0,0,0)])
b[0][0][0] = 1

while c:
    d = c.popleft()

    if d[0] == n-1 and d[1] == m-1:
        if d[2] == 0:
            print(b[n-1][m-1][0])
        else:
            print(b[n-1][m-1][1])
        exit()
    
    for x, y in h:
        x1 = d[0]+x
        y1 = d[1]+y

        if 0<= x1 < n and 0<= y1 < m and b[x1][y1][d[2]] == 0:
            if a[x1][y1] == "0":
                b[x1][y1][d[2]] = b[d[0]][d[1]][d[2]] +1
                c.append((x1, y1, d[2]))
            if a[x1][y1] == "1" and d[2] == 0:
                b[x1][y1][1] = b[d[0]][d[1]][d[2]] +1
                c.append((x1, y1, 1))


print(-1)