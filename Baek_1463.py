import sys

n = int(input())

if n == 1:
    print(0)
    exit()

if n < 4:
    print(1)
    exit()

a = [0 for i in range(n+1)]
a[2] = 1
a[3] = 1

for i in range(4,n+1):
    if i % 3 == 0:
        a3 = a[i//3]
    else:
        a3 = sys.maxsize

    if i % 2 == 0:
        a2 = a[i//2]
    else:
        a2 = sys.maxsize
    
    a[i] = (min(a3, a2, a[i-1])+1)
print(a[n])