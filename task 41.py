list=[42,36,28,96,4,-1,1]
s=0
mini=999
max=-999
for i in range(0,len(list)):
    if list[i]<mini:
        mini=list[i]
    if list[i]>max:
        max=list[i]
s=mini+max
print(s)