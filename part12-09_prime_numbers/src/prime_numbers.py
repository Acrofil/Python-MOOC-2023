# Write your solution here
def find_prime(num, start):
     
     end = num - 1 #set end 
     for i in range(start, end):#loop from start to num - 1 - end
          if num == 2: 
               return num
          
          if num % i == 0: # if num % i in the range 2 to num - 1 this is not prime number
               return 0 #return 0
          
     return num # else its prime number and  return it
          
           

def prime_numbers():
    
    number = 2 # initiliase number value to 2
    count = 2 # set count to 2
    while True: # loop forever

        prime_number = find_prime(number, count) # call helper func to find prime number pass number and count as parameters

        if prime_number != 0: # if its 0 its not prime number
            yield prime_number # yield the prime number
        
        number += 1 #increment number so when next() it will be +1
            
            
if __name__ == "__main__":
    numbers = prime_numbers() # call func prime numbers
    for i in range(8): # itterate 8 times
        print(next(numbers)) # call numbers each time
