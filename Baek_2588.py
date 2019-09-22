a = int(input())
b = int(input())

print("{}\n{}\n{}\n{}".format(a*(b%10), a*((b//10)%10), a*(b//100), a*b))