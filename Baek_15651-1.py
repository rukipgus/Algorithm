n = list(map(int, input().split()))
d = []

def per(a,b):
    if b != n[1]-1:
        for i in range(1, n[0]+1):
            d.append(i)
            per(a, b+1)
            del d[b]

    else:
        for i in range(1, n[0]+1):
            d.append(i)
            for j in range(n[1]):
                print(d[j], end = " ")
            print()
            del d[b]

per(n[0], 0)