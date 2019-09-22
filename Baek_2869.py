a, b, v = map(int, input().split())
k=v-a
u=a-b

if k%u == 0:
    print(k//u+1)
else:
    print(k//u+2)