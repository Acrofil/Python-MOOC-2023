# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

    def __str__(self):

        return f"{self.__model}, {self.__speed} MHz"


class LaptopComputer(Computer):

    def __init__(self, model: str, speed: int, weight: int):

        super().__init__(model, speed)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    def __str__(self):

        return f"{super().__str__()}, {self.__weight} kg"



if __name__ == "__main__":

    laptop = LaptopComputer("C65", 1, 10)
    print(laptop)
