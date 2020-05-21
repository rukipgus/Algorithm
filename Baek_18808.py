import sys

n, m, k = map(int, sys.stdin.readline().split())
p = [[0]* m for _ in range(n)]

def rotate_90(x):
    h = len(x)
    w = len(x[0])
    a = [[0 for i in range(h)] for _ in range(w)]
    #print(a)
    #print(x)
    #print(p)
    
    for i in range(w):
        for j in range(h):
            a[i][j] = x[h-j-1][i]
    
    #print(a)
    #print("-----------------")
    
    return a

def rotate_180(x):
    c = len(x)
    r = len(x[0])
    a = [[0]*r for _ in range(c)]

    for i in range(c):
        for j in range(r):
            a[i][j] = x[c-i][r-j]

    return a

def rotate_270(x):
    c = len(x)
    r = len(x[0])
    a = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            a[i][j] = x[r-j][i]

    return a

def rotation(x,y):
    if y == 90:
        return rotate_90(x)
    elif y == 180:
        return rotate_180(x)
    elif y == 270:
        return rotate_270(x)

def ch(x,y,m):
    r = len(m[0])
    c = len(m)
    if y + c > len(p):
        return False
    if x + r > len(p[0]):
        return False

    for i in range(c):
        for j in range(r):
            if m[i][j] == 1:
                if p[y+i][x+j] == 1:
                    return False
    
    for i in range(c):
        for j in range(r):
            if m[i][j] == 1:
                p[y+i][x+j] = m[i][j]
    
    return True

for i in range(k):
    c, r = map(int, sys.stdin.readline().split())
    a = []
    u = 0

    for j in range(c):
        a.append(list(map(int, sys.stdin.readline().split())))
    
    for e in range(4):
        if e != 0:
            a = rotate_90(a)

        for y in range(n):
            for x in range(m):
                if ch(x, y, a) == True:
                    u = 1
                    break
            if u == 1:
                break
        if u == 1:
            break

#print(p)
s = 0
for i in range(n):
    for j in range(m):
        if p[i][j] == 1:
            s += 1
print(s)