# Write your solution here
import re

def is_dotw(my_string: str):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day_found = False
    
    for word in days:
       if re.search(word, my_string):
            day_found = True


    return day_found

def all_vowels(my_string: str):
    all_vowels = True

    if re.search("[^aeiou]", my_string):
        all_vowels = False
    
    return all_vowels

def time_of_day(my_string: str):
    time = '^([0-1][0-9]|[2][0-4]):([0-5][0-9]):([0-5][0-9])$'
  
    if re.search(time, my_string):
        return True
    else:
        return False

if __name__ == "__main__":
    print(time_of_day("AB:20:20")) 
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
   
