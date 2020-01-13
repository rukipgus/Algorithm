n = list(map(int, input().split()))
d = []

def per(a,b):
    if b == n[1]:
        print(" ".join(d))
        return

    for i in range(a, n[0]+1):
        d.append(str(i))
        per(i,b+1)
        d.pop()

per(1, 0)