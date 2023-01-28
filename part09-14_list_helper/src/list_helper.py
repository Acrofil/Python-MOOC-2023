# WRITE YOUR SOLUTION HERE:

class ListHelper:

    def __init__(self, list: list):

        self.list = list

    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        
        most_repeated = 0
        times_in = 0

        for number in my_list:

            times = my_list.count(number)

            if times > times_in:
                most_repeated = number
                times_in = times

        
        return most_repeated
    
    @classmethod
    def doubles(cls, my_list: list):
        
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles

if __name__ == "__main__":

    numbers = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))