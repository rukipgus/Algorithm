import sys

t  = int(sys.stdin.readline())

for i in range(t):
    m, n, k  = map(int, sys.stdin.readline().split())
    a = []
    for j in range(k):
        b, c = map(int,sys.stdin.readline().split())
        a.append((b,c))

    u = []
    while a:
        b = []
        c = []
        c.append(a[0])
        del a[0]

        while c:
            d = c.pop()
            b.append(d)

            if (d[0]+1,d[1]) in a:
                    c.append((d[0]+1,d[1]))
                    a.remove((d[0]+1,d[1]))
            if (d[0]-1,d[1]) in a:
                    c.append((d[0]-1,d[1]))
                    a.remove((d[0]-1,d[1]))
            if (d[0],d[1]+1) in a:
                    c.append((d[0],d[1]+1))
                    a.remove((d[0],d[1]+1))
            if (d[0],d[1]-1) in a:
                    c.append((d[0],d[1]-1))
                    a.remove((d[0],d[1]-1))
        
        u.append(len(c))
    
    print(len(u))