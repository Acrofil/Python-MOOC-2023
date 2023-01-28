# WRITE YOUR SOLUTION HERE:

class Recording:

    def __init__(self, lenght: int):

        if lenght < 0:
            raise ValueError

        self.__lenght = lenght

    
    @property
    def length(self):

        return self.__lenght

    @length.setter
    def length(self, lenght: int):

        if lenght >= 0:
            self.__lenght = lenght
        else:
            raise ValueError

if __name__ == "__main__":
    
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 45
    print(the_wall.length)

        



