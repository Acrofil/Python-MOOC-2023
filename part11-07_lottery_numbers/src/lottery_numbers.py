
class LotteryNumbers:

    def __init__(self, number: int, number_list: list):
        self.number = number
        self.number_list = number_list


    def number_of_hits(self, numbers: list):
        
        return len([number for number in numbers if number in self.number_list])


    def hits_in_place(self, numbers):

        return [number if number in self.number_list else -1 for number in numbers]

if __name__ == "__main__":

    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))
