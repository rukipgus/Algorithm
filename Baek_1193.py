a = int(input())
n = 1

while True:
    if a <= n*(n+1)/2:
        break
    n+=1

if n%2 == 0:
    print("{}/{}".format((a-n*(n-1)//2),n+1-(a-n*(n-1)//2)))
else:
    print("{}/{}".format(n+1-(a-n*(n-1)//2), (a-n*(n-1)//2)))