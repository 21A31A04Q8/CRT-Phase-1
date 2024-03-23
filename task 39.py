list=[]
list=[67,"lavanya",3.4,True,"usha"]
print(list[4])
print(list[3])
list.append(90)
list.insert(0,"lucky")
for i in range(0,len(list)):
    print(list[i])
print(list[0:6])
print(list[6:1:-1])
print(list[4:])
print(list[:4])
print(list[:])
list[4]="8"
print(list)