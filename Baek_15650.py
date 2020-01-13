c, d = map(int, input().split())

p = []

def per(a, b):
    if b == 0:
        for i in range(1, c+1):
            p.append(i)
            per(a, b+1)
            del p[b]

    elif b == d-1:
        for i in range(p[b-1]+1, c+1):
            for j in range(d):
                p.append(i)
                print(p[j], end = " ")
                del p[b]
            print()
    else:
        for i in range(p[b-1]+1, c+1):
            p.append(i)
            per(a, b+1)
            del p[b]

if d == 1:
    for i in range(1, c+1):
        print(i)

else:
    per(c, 0)
