# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        

    def __str__(self):
        return self.name

class Room:

    def __init__(self):

        self.persons = []
        self.people_in_room = 0
        self.total_height = 0

    def add(self, person: Person):
        
        self.persons.append(person)
        self.total_height += person.height
        self.people_in_room += 1

    def is_empty(self):
        
        if self.people_in_room == 0:
            return True
        else:
            return False

    def print_contents(self):

        print(f"There are {self.people_in_room} persons in the room, and their combined height is {self.total_height} cm")

        for person in self.persons:

            print(f"{person} ({person.height} cm)")

    def shortest(self):

        height = 0

        if self.people_in_room == 0:
            return None

        for person in self.persons:
                if person.height > 0 and height != 0:
                    if person.height < height:
                        height = person.height
                        the_shortest = person
                elif person.height > 0 and height == 0:
                    height = person.height
                    the_shortest = person
        

        return the_shortest

        

    def remove_shortest(self):

        shortest_person = self.shortest()

        if self.people_in_room == 0:
            return None
        else:

            for index, person in enumerate(self.persons, start=0):
                if person == shortest_person:
                    remove = self.persons.pop(index)
                    self.total_height -= person.height
                    self.people_in_room -= 1

                    return remove
    

if __name__ == "__main__":

    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()