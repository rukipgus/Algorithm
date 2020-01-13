import sys
import math

a = int(input())

for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    
    if b[0] == b[3] and b[1] == b[4]:
        if b[2] == b[5]:
            print(-1)
        else:
            print(0)
 
    else:       
        d1 = math.sqrt(pow(b[3]-b[0],2)+pow(b[4]-b[1],2))

        if d1 == abs(b[2]-b[5]) or d1 == (b[2]+b[5]):
            print(1)

        elif d1 > b[2] and d1 > b[5]:
            if d1 > b[2]+b[5]:
                print(0)
            else:
                print(2)
                    
        else:
            if d1 < abs(b[2]-b[5]):
                print(0)
            else:
                print(2)