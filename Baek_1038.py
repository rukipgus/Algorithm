n = int(input())
c = 0
k = 1

while True:
    t = str(k)
    u = list(t)
    p = 0
    for i in range(len(u)-1):
        if int(u[i]) <= int(u[i+1]):
            p = 1
            break
        
    if p == 0:
        c += 1
        if c == n:
            break
    k += 1             

print(k)