class MinBalance(Exception):
    
    def _str_(self):
        return "MinBalance try again!"

class account:
    account_n=101
    
    def _init_(self,name,acc_n,balance=1000):
        try:
            if balance<1000:
                raise MinBalance()
        except MinBalance as e:
            print(e)
        self.name=name
        self.balance=balance
        self.acc_n=account.account_n
        account.account_n+=1
        
    def deposit(self,amt):
        self.balance+=amt
    
    def withdraw(self,amt):
        try:
            if self.balance-amt<1000:
                    raise MinBalance()
        except MinBalance as e:
            print(e)
            
        self.balance-=amt
    
    def showdetails(self):
        print("name",self.name)
        print("acc_number",self.acc_n)
        print("balance",self.balance)
            
a=account("vijay",2000)
a.showdetails()
a.withdraw(2000)
