p = []
c, d = map(int, input().split())

def pr(a, b):
    if b == 1:
        for i in range(1,a+1):
            if p.count(i) == 0:
                p.append(i)
                for j in range(d):
                    print(p[j], end = " ")
                print()
                del p[d-b]
    else:
        for i in range(1,a+1):
            if p.count(i) != 0:
                continue
            else:
                p.append(i)
                pr(a, b-1)
                del p[d-b]

pr(c, d)