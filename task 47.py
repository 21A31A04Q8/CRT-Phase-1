def login():
    n=1
    while n!=0:
        username=input("enter username")
        pwd=input("enter pwd")
        if username==pwd:
            print("logged in")
            break
        else:
            print("invalid")
login()
        
    