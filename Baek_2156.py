import sys

n = int(sys.stdin.readline())
a = [0]
b = [0]

for i in range(n):
    a.append(int(sys.stdin.readline()))
    b.append(0)

b[1] = a[1]

if n > 1:
    b[2] = a[1]+a[2]

for i in range(3, n+1):
    b[i] = max(a[i]+a[i-1]+b[i-3], a[i]+b[i-2],b[i-1])

print(b[-1])