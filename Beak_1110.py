a = int(input())
c = a
if a >= 0 and a < 100:
    i = 0
    while True:
        b=(c//10)+(c%10)
        c =(c%10)*10+(b%10)
        i+=1
        if c == a:
            print(i)
            exit()
else:
    exit()