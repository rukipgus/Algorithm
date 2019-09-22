a = int(input())
b = a//5

for i in range(b+1):
    if (a-5*(b-i))%3 == 0:
        print(b-i + (a-5*(b-i))//3)
        exit()
print(-1)