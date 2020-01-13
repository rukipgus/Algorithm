import copy

n = int(input())
im = [[True for i in range(n)] for j in range(n)]
an = [0]

def chq(x,y,matr):
    mat = copy.deepcopy(matr)

    for i in range (n):
        mat[i][y] = False
        mat[x][i] = False
        if 0<=(x+i)<n and 0<=(y+i)<n:
            mat[(x+i)][(y+i)] = False
        if 0<=(x-i)<n and 0<=(y-i)<n:
            mat[(x-i)][(y-i)] = False
        if 0<=(x+i)<n and 0<=(y-i)<n:
            mat[(x+i)][(y-i)] = False
        if 0<=(x-i)<n and 0<=(y+i)<n:
            mat[(x-i)][(y+i)] = False
    return mat

#(n+1)//2
def queen(a, b):
    if b == 0:
        for i in range(n):
            for j in range(n):
                #for i in range(n):
                #    print(a[i])
                d = chq(i,j,a)
                queen(d,b+1)
        
    elif b == n:
        #for i in range(n):
        #    print(a[i])
        an[0] += 1
        #print("got")
        return
    else:
        #for i in range(n):
            #print(a[i])
        for i in range(n):
            for j in range(n):
                if a[i][j] == True:
                    d = chq(i,j,a)
                    queen(d,b+1)

queen(im, 0)
k = an[0]
for i in range(1, n+1):
    k = k//i

print(k)