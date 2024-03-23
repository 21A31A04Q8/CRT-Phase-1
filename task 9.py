m=int(input("enter marks="))
n=int(input("enter marks="))
o=int(input("enter marks="))

if (m and n and o)>80:
    print("a+")
elif ((m and n and o)>60 and (m and n and o)<80):
    print("b+")
else:
    print("pass")
