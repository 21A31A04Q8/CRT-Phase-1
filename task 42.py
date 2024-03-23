d={"name":"asha","rollno":"q8","address":"hyd",239:"h","123":9}
d["123"]=99
d[100]=34
for i in d:
    print(i)
for x in d.values():
    print(x)
for x,y in d.items():
    print(x,y)
d.pop("name")
print(d)