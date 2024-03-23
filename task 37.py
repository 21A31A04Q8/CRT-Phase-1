n=153
s=0
c=0
n1=n
org=n
while n>0:
    n=n//10
    c=c+1
while n1>0:
    d=n1%10
    s=s+(d**c)
    n1=n1//10
if s==org:
    print("yes") 
else:
    print("no")
print(s)