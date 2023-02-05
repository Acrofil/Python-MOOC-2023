# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    
    def __init__(self, day: int, month: int, year: int):

        self.day = day
        self.month = month
        self.year = year
        self.date = f"{self.day}.{self.month}.{self.year}"

    def convert_to_days(self):

        days = (self.month * 30) + (self.year * 360) + self.day

        return days  
    
    def __str__(self) -> str:
        
        return f"{self.day}.{self.month}.{self.year}"


    def __eq__(self, other):

        if self.convert_to_days() == other.convert_to_days():
            return True
        else:
            return False

    def __ne__(self, other):

        if self.convert_to_days() != other.convert_to_days():
            return True
        else:
            return False

    def __lt__(self, another):

        if self.convert_to_days() < another.convert_to_days():
            return True
        else:
            return False


    def __gt__(self, another):

        if self.convert_to_days() > another.convert_to_days():
            return True
        else:
            return False

    def __add__(self, another):

        self.new_day = self.day
        self.new_month = self.month
        self.new_year = self.year
        
        for day  in range(another):

            if self.new_day == 30:
                self.new_day = 0
                self.new_month += 1
            
            if self.new_month == 12:
                self.new_month = 0
                self.new_year += 1

            
            self.new_day += 1

        
        return SimpleDate(self.new_day, self.new_month, self.new_year)

    
    def __sub__(self, another):

        self.difference = 0

        self.difference = abs(self.convert_to_days() - another.convert_to_days())

        return self.difference



if __name__ == "__main__":

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)