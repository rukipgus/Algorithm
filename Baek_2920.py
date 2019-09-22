a = input()
b = "12345678"
c = "87654321"

a = a.replace(" ","")
    
if a == b:
    print("ascending")
elif a == c:
    print("descending")
else:
    print("mixed")