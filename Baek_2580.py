import sys

def sd(x,y,z): #x리스트　y행렬 z순번
    if z == len(x):
        v = []
        for i in range(9):
            for j in range(9):
                if y[i][j] == 0:
                    v.append([i,j])
        if len(v) == 0:
            sd(v,y,0)
        else:
            for i in range(9):
                for j in range(9):
                    print(y[i][j], end = " ")
                print()
            exit()

    for i in range(z, len(x)):
        a = {1,2,3,4,5,6,7,8,9}
        b = set()

        for j in range(9):
            b.add(y[x[i][0]][j])
            b.add(y[j][x[i][1]])

        for j in range(3):
            for k in range(3):
                b.add(y[3*(x[i][0]//3)+j][3*(x[i][1]//3)+k])
        
        a = list(a-b)

        for j in a:
            y[x[i][0]][x[i][1]] = j
            sd(x,y,z+1)

a = []
b = []

for i in range(9):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if a[i][j] == 0:
            b.append([i,j])

sd(b,a,0)