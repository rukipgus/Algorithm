n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [i for i in b]

def per(x,y,u):
    if y == (u-1):
        u.add(x)
    
    for i in range(u-1):
        




ma = 0
mi = 0
d = a[0]
e = a[0]




for i in range(n-1):
    if b[1] > 0:
        d -= a[i+1]
        b[1] -=1
        print("max:-")
    elif b[3] > 0:
        d //= a[i+1]
        b[3] -=1
        print("max://")
    elif b[0] > 0:
        d += a[i+1]
        b[0] -=1
        print("max:+")
    elif b[2] > 0:
        d *= a[i+1]
        b[2] -=1
        print("max:*")

for i in range(n-1):
    if c[0] > 0:
        e += a[i+1]
        c[0] -=1
        print("min:+")
    elif c[3] > 0:
        e //= a[i+1]
        print("min://")
        c[3] -=1
    elif c[1] > 0:
        e -= a[i+1]
        c[1] -=1
        print("min:-")
    elif c[2] > 0:
        e *= a[i+1]
        c[2] -=1
        print("min:*")

print(d)
print(e)