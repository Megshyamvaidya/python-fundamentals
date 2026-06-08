class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount<0:
            print("Balance cannot be negative")
        else:
            self.__balance=amount
    
    def deposit(self,amount):
        if amount>0:
            self.__balance=amount+self.__balance
            print(f"Deposited {amount}|New balance:{self.__balance}")
        else:
            print("Amount must be greater than 0")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient funds")
        else:
            self.__balance=self.__balance-amount
            print(f"Withdrawal amount {amount}|New balance: {self.__balance}")
    def __str__(self):
        return f"Account[{self.owner}]|Balance[{self.__balance}]"
    @classmethod
    def from_dict(cls,data):
        return cls(data["owner"],data["balance"])
c1=BankAccount("Megshyam",80000)
print(c1.balance)
c1.balance=-77
print(c1.balance)
c1.deposit(60000)
c1.withdraw(76544)
print(c1)
data={"owner":"Rahul",'balance':80000}
c2=BankAccount.from_dict(data)
print(c2)