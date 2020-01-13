import copy

n = int(input())
a = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
    s = copy.deepcopy(a)
    a[0] = s[1]
    for j in range(1,9):
        a[j] = s[j-1]+s[j+1]
    a[9] =s[8]

print(sum(a)%1000000000)