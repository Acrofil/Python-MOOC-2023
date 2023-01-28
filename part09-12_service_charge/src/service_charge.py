# WRITE YOUR SOLUTION HERE:
import math
class BankAccount:

    def __init__(self, name: str, account_number: str, balance: float):

        self.__name = name
        self.__account_number = account_number
        self.__balance = balance


    def deposit(self, amount: float):

        if amount >= 0:

            self.__balance += amount
            self.__service_charge()
            
        else:
            raise ValueError
    def withdraw(self, amount: float):

        if amount >= 0:
            
            self.__balance -= amount
            self.__service_charge()
            
        else:
            raise ValueError

    def __service_charge(self):
        
        charge = self.__balance * 0.010
        self.__balance -= charge


    @property
    def balance(self):

        return self.__balance

    


if __name__ == "__main__":

    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)