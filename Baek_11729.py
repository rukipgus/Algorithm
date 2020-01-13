n = int(input())

def hanoi(a,b,c,k,t):
    if k == 0:
        print(t)
        return
    