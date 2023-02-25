# WRITE YOUR SOLUTION HERE:
import math

#Receive list of numbers
def square_roots(numbers: list):


    return [math.sqrt(number) for number in numbers] #List comprehension call math.sqrt and loop tru the list and return new list


if __name__ == "__main__":

    lines = square_roots([1,2,3,4]) #Send numbers
    for line in lines: #loop tru the new list from list comprehension
        print(line)
