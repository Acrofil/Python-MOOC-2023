# TEE RATKAISUSI TÄHÄN:
import math

class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__pr = f"{self.__euros}.{self.__cents:02}"
        self.__price = float(self.__pr)
        self.__total_sum = 0

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"


    def __eq__(self, another):

       if self.__price == another.__price:
        return True
       else:
        return False

    def __lt__(self, another):

        if self.__price <  another.__price:
            return True
        else:
            return False

    def __gt__(self, another):

        if self.__price > another.__price:
            return True
        else:
            return False

    def __ne__(self, another):
        
        if self.__price != another.__price:
            return True
        else:
            return False
    
    def __add__(self, another):


        self.__total_sum = self.__price + another.__price
        self.__total_sum = format(self.__total_sum, '.2f')


        return f"{self.__total_sum} eur"
        

    def __sub__(self, another):

        self.__total_sum = round(self.__price - another.__price, 2)
        self.__total_sum = format(self.__total_sum, '.2f')

        if float(self.__total_sum) < 0:
            raise ValueError
        else:
            return f"{self.__total_sum} eur"





if __name__ == "__main__":

    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
    
    
