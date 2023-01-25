class Person:

    def __init__(self, name):
        self.name = name

    def return_first_name(Person):
        first_name = Person.name.split()

        return first_name[0]

    def return_last_name(Person):

        lst_name = Person.name.split()

        return lst_name[1]



if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())





