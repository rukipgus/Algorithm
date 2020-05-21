import sys

n = int(sys.stdin.readline())
p = []
v = []

def qt(x, y, z):
    a = 0
    b = 0
    c = 0

    for i in range(y, y+z):
        for j in range(x, x+z):
            #print("x:",j ,"y:",i, "n:", z)
            #print("".join(v))

            if p[i][j] == "0":
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
            v.append("0")
        else:
            v.append("1")
    
    else:
        v.append("(")
        qt(x, y, z//2)
        qt(x+ (z//2), y, z//2)
        qt(x, y+ (z//2), z//2)
        qt(x + (z//2), y + (z//2), z//2)
        v.append(")")
                
for i in range(n):
    p.append(list(sys.stdin.readline().rstrip()))

qt(0,0,n)
print("".join(v))
