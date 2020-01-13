a = list(map(int, input().split()))
b = min(a[1], a[0]-a[1])
f = max(a[1], a[0]-a[1])
c = [0,0]
e = [0,0]
g = [0,0]
d = 5
h = 2

for i in range(200):
    if h <= b:
        g[1] += b // h
    
    if d <= b:
        g[0] += b // d

    if h <= f:
        e[1] += f // h

    if d <= f:
        e[0] += f // d

    if d <= a[0]:
        c[0] += a[0] // d

    if h <= a[0]:
        c[1] += a[0] // h
    else:
        break

    d *= 5
    h *= 2

print(min((c[0] - g[0] - e[0]),(c[1] - g[1] - e[1])))