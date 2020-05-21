n = int(input())
a = []

def hano(n, x, y, z):
    if n == 1:
        a.append([x,z])
        return
    hano(n-1, x, z, y)
    a.append([x,z])
    hano(n-1, y, x, z)

hano(n, 1,2,3)

print(len(a))
print("\n".join(   [" ".join([str(i) for i in c]) for c in a ))