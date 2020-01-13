import sys

n = int(sys.stdin.readline())
b =[0,0,0]

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    c = [0,0,0]
    c[0] = b[0]
    c[1] = b[1]
    c[2] = b[2]

    b[0] = a[0]+ min(c[1],c[2])
    b[1] = a[1]+ min(c[0],c[2])
    b[2] = a[2]+ min(c[0],c[1])

print(min(b))
    
