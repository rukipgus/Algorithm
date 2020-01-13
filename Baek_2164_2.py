import collections

n = int(input())
deq = collections.deque([i for i in range(1,n+1)])

while len(deq) != 1:
    deq.popleft()
    deq.rotate(-1)

print(deq[0])