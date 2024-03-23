class car:
    def __init__(self):
        self.cgst=0.5
        self.sgst=0.5
        self.insurance=9000
    def company(self):
        while True:
            print("toyota,mercedes")
            self.n=input("enter the car company")
            if self.n=="toyota":
                print("welcome to toyota")
                self.model()
                break
            elif self.n=="mercedes":
                print("welcome to mercedes")
                self.model()
                break
            else:
                print("enter valid company")
    def model(self):
        if self.n=="toyota":
            while True:
                print("select from fortuner and LC")
                self.choice=input("enter the car model")
                if self.choice=="fortuner":
                    self.price(self.choice)
                elif  self.choice=="LC":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid")
        elif self.n=="mercedes":
            while True:
                print("select from amg and gw")
                self.choice=input("enter the car model")
                if self.choice=="amg":
                    self.price(self.choice)
                elif self.choice=="gw":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid")
    def price(self,choice):
        if choice=="fortuner":
            self.p=4500000
        elif choice=="LC":
            self.p=10000000
        elif choice=="awg":
            self.p=3478028
        elif choice=="gw":
            self.p=4378909
        tot_p=self.p+self.cgst+self.sgst+self.insurance
        print(tot_p)  
c=car() 
c.company()            