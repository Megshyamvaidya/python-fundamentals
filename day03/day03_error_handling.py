# # print(10/0)
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Cannot divide by Zero")

# try:
#     name='Megshyam'
#     print(name+100)
# except TypeError:
#     print("Wrong data tyoe used")

# try:
#     numbers=[1,2,3]
#     print(numbers[10])
# except IndexError:
#     print("Index out of range")

# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Cannot divide by 0")
# else:
#     print(f"Result is {result}")
# finally:
#     print("This always runs error or not")

# def divide(a,b):
#     try:
#         result=a/b
#     except ZeroDivisionError:
#         print("Cannot divide by 0")
#     except TypeError:
#         print("input must be integers")
#     else:
#         print(f"Result is {result}")
#     finally:
#         print("Division attempted")
# divide(10,2)
# divide(10,'w')
# divide(10,0)
# # custom exceptions
# # for bank management project
# class InsufficientFundsError(Exception):
#     def __init__(self,balance,amount):
#         self.balance= balance
#         self.amount= amount
#         super().__init__(f"cannot withdraw {amount}. Current balancei s{balance}")

# class InvalidAmountError(Exception):
#     def __init__(self, amount):
#         self.amount = amount
#         super().__init__(f"Invalid amount {amount}")



# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner= owner
#         self.__balance= balance

#     @property
#     def balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         try:
#             if amount<=0:
#                 raise InvalidAmountError(amount)
#             self.__balance+=amount
#             print(f"Deposited {amount}|New balance {self.__balance}")
#         except InvalidAmountError as e:
#             print(e)
#     def withdraw(self,amount):
#         try:
#             if amount<=0:
#                 raise InvalidAmountError(amount)
#             if amount>self.__balance:
#                 raise InsufficientFundsError(self.__balance,amount)
#             self.__balance-=amount
#             print(f"Withdrawn amount {amount} | Remaining {amount}")
#         except InvalidAmountError as e:
#             print(e)
#         except InsufficientFundsError as e:
#             print(e)
#     def __str__(self):
#         return (f"Account[{self.owner}] | Balance [{self.__balance}]")
    
# c1=BankAccount("Megshyam",80000)
# c1.deposit(700)
# c1.deposit(-876)
# c1.withdraw(44045)
# c1.withdraw(99999)
# c1.withdraw(-322)
# print(c1)




# assignment

def safe_divide():
    try:
        a=int(input("Enter number 1 ="))
        b=int(input("Enter number 2 ="))
    
        result=a/b
    except ZeroDivisionError :
        print("Cannot divide by 0")
    except ValueError:
        print("Enter numbers only")
    else:
        print(f"Result :{result}")
    finally:
        print("Calculation completed")
safe_divide()
