def han(x):
    b = [int(i) for i in str(x)]
    c=b[1]-b[0]

    for i in range(1,len(b)-1):
        if c != b[i+1] - b[i]:
            return 0
    return 1



a = int(input())
count = 99

if len(str(a)) < 3:
    print(a)
    exit()

else:
    for i in range(100,a+1):
        count += han(i)

print(count)