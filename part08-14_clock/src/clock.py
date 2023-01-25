# Write your solution here:
# Write your solution here:
from datetime import time

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set(self, hour: int, minutes: int):
        self.hours =  hour
        self.minutes = minutes
        self.seconds = 0

    def tick(self):

        if self.seconds < 59:

            self.seconds += 1    
        elif self.seconds == 59:

            self.seconds = 0
            self.minutes += 1

        if self.minutes > 59:

            self.minutes = 0
            self.hours += 1

        elif self.hours == 24:
            self.hours = 0
        


    def    __str__(self):

        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


if __name__ == "__main__":

        clock = Clock(23, 59, 55)
        print(clock)
        clock.tick()
        print(clock)
        clock.tick()
        print(clock)
        clock.tick()
        print(clock)
        clock.tick()
        print(clock)
        clock.tick()
        print(clock)
        clock.tick()
        print(clock)

        clock.set(12, 5)
        print(clock)

        
        
