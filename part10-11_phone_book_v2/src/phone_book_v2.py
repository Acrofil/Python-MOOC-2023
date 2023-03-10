# Write your solution here:
 
class Person:
    def __init__(self, name: str):
 
        self.__person_name = name
        self.__person_numbers = []
        self.__person_address = None
 
    def name(self):
 
        return self.__person_name
    
    def numbers(self):

 
        return self.__person_numbers
    
    def address(self):
 
        if self.__person_address == None:
            return None
    
 
        return self.__person_address
    
    def add_number(self, number: str):
        self.__person_numbers.append(number)
 
    def add_address(self, address: str):
        self.__person_address = address
 
class PhoneBook():
    def __init__(self):
        self.__persons = {}
 
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)
               
 
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
    
 
    def all_entries(self):
        return self.__persons
 
 
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
 
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")
 
    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
 
    def search(self):
        name = input("name: ")
        data = self.__phonebook.get_entry(name)
 
        if data == None:
            print("address unknown")
            print("number unknown")
            return

        numbers = data.numbers()
 
        if len(numbers) == 0:
            print("number unknown") 
        else:
            for number in numbers:
                print(number)       
        
        address = data.address()
 
        if address == None:
            print("address unknown")
        else:
            print(address)
    
    def add_address(self):
        name = input("name:")
        address = input("address:")
        self.__phonebook.add_address(name, address)
 
 
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
 
 
 #when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()