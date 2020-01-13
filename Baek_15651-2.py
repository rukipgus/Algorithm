n = list(map(int, input().split()))
d = []

def per(a,b):
    if b == n[1]:
        print(" ".join(d))
        return
    
    for i in range(1,a+1):
        d.append(str(i))
        per(a, b+1)
        d.pop()

per(n[0], 0)