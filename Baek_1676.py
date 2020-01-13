n = int(input())
a = 1

for i in range(1,n+1):
    a *= i

a = str(a)
b = 0

if n < 4:
    print(0)

for i in a[-1:0:-1]:
    if i == "0":
        b += 1
    else:
        print(b)
        break