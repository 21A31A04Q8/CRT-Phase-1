tuple=("asha",33,True,"anchal","bharu")
print(tuple)
print(type(tuple))
tuple=tuple+(44,77)
print(tuple)
for i in range(0,5):
    n=int(input("enter"))
    tuple=tuple+(n,)
    print(tuple)