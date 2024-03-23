m=int(input("enter a value :"))
if m%3==0 and m%5==0:
    print("great")
elif m%3==0 and m%9==0:
    print("good")
elif m%3==0 and m%7==0:
    print("ok")
else:
    print("not ok")
