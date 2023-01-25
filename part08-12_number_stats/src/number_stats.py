# Write your solution here!

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.total_sum = 0
        self.avg = 0
        self.sum_even = 0
        self.sum_odd = 0

    def even(self):

        return self.sum_even
    
    def odd(self):

        return self.sum_odd


    def add_number(self, number:int):
        
        self.count += 1
        self.total_sum += number

        if number % 2 == 0:

            self.sum_even += number
        else:
            self.sum_odd += number
        
        

    def count_numbers(self):
        

        return self.count

    def get_sum(self):

        if self.count == 0:
            return 0

        return self.total_sum


    def average(self):


        if self.total_sum == 0:
            return 0


        self.avg = self.total_sum / self.count

        return self.avg



def main():

    st = NumberStats()
    print("Please type in integer numbers: ")
    while True:

        num = int(input())

        if num == -1:
            break

        st.add_number(num)
    
    print(f"Sum of numbers: {st.get_sum()}")
    print(f"Mean of numbers: {st.average()}")
    print(f"Sum of even numbers: {st.even()}")
    print(f"Sum of odd numbers: {st.odd()}")

main()