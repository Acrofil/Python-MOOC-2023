class Item:

   def __init__(self, name: str, weight: int):

        self.__name = name
        self.__weight = weight

   def name(self):

        return self.__name
    
   def weight(self):

        return self.__weight

   def __str__(self):

    
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:

    def __init__(self, max_weight: int):

        self.max_weight = max_weight
        self.kg_in_suitcase = 0
        self.total_items = 0
        self.added_items = []

    def add_item(self, item: Item):


        if item.weight() < self.max_weight:
            self.added_items.append(item)
            self.max_weight -= item.weight()
            self.kg_in_suitcase += item.weight()
            self.total_items += 1

    def print_items(self):

        for item in self.added_items:

            print(item)

    def weight(self):

        return self.kg_in_suitcase

    def __str__(self):

        if self.total_items == 1:

            return f"{self.total_items} item ({self.kg_in_suitcase} kg)"
        else:
            return f"{self.total_items} items ({self.kg_in_suitcase} kg)"

    def heaviest_item(self):

        if len(self.added_items) == 0:
            return None
        
        heaviest = 0

        for item in self.added_items:
            
            if item.weight() > heaviest:
                heaviest = item.weight()
                most_heavy = item
        

        return most_heavy

class CargoHold:

    def __init__(self, max_weight: int):

        self.max_weight = max_weight
        self.cargohold = []
        self.suitaces_added = 0

    def add_suitcase(self, suitcase: Suitcase):

       if suitcase.weight() < self.max_weight:
            self.cargohold.append(suitcase)
            self.max_weight -= suitcase.weight()
            self.suitaces_added += 1

    def  print_items(self):

        for item in self.cargohold:

            item.print_items()


    def __str__(self):

        if self.suitaces_added == 1:

            return f"{self.suitaces_added} suitcase, space for {self.max_weight} kg"
        else:

            return f"{self.suitaces_added} suitcases, space for {self.max_weight} kg"

if __name__ == "__main__":

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()





