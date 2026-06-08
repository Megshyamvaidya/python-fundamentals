class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Account[{self.owner}]|Balance:{self.balance}"
    def introduce(self):
        print(f"Owner is {self.owner} and his current balance is {self.balance}")
        # print(f"Current Balance {self.balance}")

    # deposit amount
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposited amount {amount}|New balance={self.balance}")

    # withdraw amount

    def withdraw(self,amount):
        
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f"Withdrawal successful rupees {amount} and balance is",self.balance)

        else:
            print("Insufficient Funds in account ")
#interest fetcher 
class SavingsAccount(BankAccount):
    def __init__(self, owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
    # adding interest 
    def add_interest(self):
        interest=self.balance*(self.interest_rate/100)
        self.balance=self.balance+interest
        print(f"Interest added : {interest}| New balance={self.balance}")
# creating objects
c1=BankAccount("Megshyam",70000) 
c1.introduce()
c1.deposit(2000)
c1.withdraw(10000)

d1=SavingsAccount("Megshyam",100000,3)
d1.interest_rate=7
d1.add_interest()
print(c1)
