import collections
import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    deq = collections.deque(list(map(int, sys.stdin.readline().split())))
    d = b
    e = 0
    
    while len(deq) != 0:
        c = max(deq)
        if deq[0] == c:
            if d == 0:
                print(e+1)
                break
            else:
                deq.popleft()
                e +=1
                d -= 1
        else:
            if d == 0:
                deq.rotate(-1)
                d = (len(deq)-1)
            else:
                deq.rotate(-1)
                d -= 1