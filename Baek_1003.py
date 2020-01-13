import sys
p = []

def ch(n):
    a = [1,0]
    b = [0,1]

    for i in range(n):
        t = a[0]
        a[0] = b[0]
        b[0] = t+b[0]

        t = a[1]
        a[1] = b[1]
        b[1] = t+b[1]
        
    print(a[0], b[0])
    
n = int(input())

for i in range(n):
    p.append(int(sys.stdin.readline()))

for i in p:
    ch(i)
