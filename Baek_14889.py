import sys

def spt(x,y,z,u,p): #x후보 y길이 z크기 u최대값 p행렬
    if len(x) == z//2:
        c = 0
        d = [i for i in range(z)]
        d = list(set(d)-set(x)) 

        for i in range(z//2):
            for j in range(i+1,z//2):
                c += p[x[i]][x[j]]
                c += p[x[j]][x[i]] 
                c -= p[d[i]][d[j]]
                c -= p[d[j]][d[i]]

        if abs(c) < u[0]:
            u[0] = abs(c)
        
        return 

    for i in range(y,z):
       x.append(i)
       spt(x,i+1,z,u,p)
       del x[-1] 

n = int(input())
a = []
k = [sys.maxsize]

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

spt([],0,n,k,a)
print(k[0])