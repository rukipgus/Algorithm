import sys

n = int(sys.stdin.readline())
p = []
d = [0,0]

for i in range(n):
    p.append(list(map(int, sys.stdin.readline().split())))

def ch(x,y,z):
    a = 0
    b = 0
    c = 0

    for i in range(y,y+z):
        for j in range(x, x+z):
            #print("x:", j, "y:", i, "n:",z)
            if p[i][j] == 0:
                a = 1
            else:
                b = 1
            if a == 1 and b == 1:
                c = 1
                break
        if c == 1:
            break
    
    if c == 0:
        if a == 1:
            #print("white")
            d[0] += 1
        else:
            d[1] += 1
            #print("black")
    else:
        ch(x , y, z//2)
        ch(x + z//2, y, z//2)
        ch(x, y + z//2, z//2)
        ch(x + z//2, y + z//2, z//2)

ch(0,0,n)

print(d[0])
print(d[1])