import sys

n, k = map(int, sys.stdin.readline().split())
a = [[0,0]]
b = [0]*(k+1)

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,n+1):
    c = [0]*(k+1)
    for j in range(k-a[i][0]+1):
        print(i)
        c[a[i][0]+j] = max(a[i][1]+b[j],b[a[i][0]+j])
    for j in range(len(c)):
        if c[j] != 0:
            b[j] = c[j]

print(b)

print(max(b))
