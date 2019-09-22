a = int(input())
i = 0

if a == 1:
    print(1)
    exit()
    
while True:
    if (a > (1+3*i*(i+1))) and (a <= 1+3*(i+1)*(i+2)):
        print(i+2)
        break
    i+=1