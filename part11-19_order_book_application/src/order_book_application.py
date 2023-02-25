# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task: #Main class Task for each individual task

    program_id = 0 #Class variable to store the program id
    def __init__(self, description: str, programmer: str, workload: int):
        
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.program_status = False
        Task.program_id += 1 #Class variable
        self.id = Task.program_id #Set id for individual program in order

        
    def id(self):
        
        return self.id

    def mark_finished(self):
        self.program_status = True


    def is_finished(self):
        return self.program_status
    
    
    def __str__(self) -> str:

        program_end = 'FINISHED'if self.program_status == True else 'NOT FINISHED' #Check if program has finished or unfinished

        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {program_end}" #Return str repr
    
class OrderBook: #New class for storing each programming task as object

    def __init__(self):
        self.__orders = [] #List to store all programming tasks
        

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload) #Create new object with the help of Task class
        self.__orders.append(order) #Add to the list

    def all_orders(self):
        return [order for order in self.__orders] #Returns all stored tasks
    
    def programmers(self):
          return list(set([order.programmer for order in self.__orders])) #Returns all programmers that take part using set to remove duplicates
    
    def mark_finished(self, id: int): #Marks task as finished

        id_found = False

        for order in self.__orders:
            if order.id == id:
                id_found = True

        if id_found == False:
            raise ValueError(f"Order with {id} not found")

        return [order.mark_finished() for order in self.__orders if order.id == id]

    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished() == True] #Returns finished tasks

    def unfinished_orders(self):
        return [order for order in self.__orders if order.is_finished() == False] #Returns unfinished tasks
    
    def status_of_programmer(self, programmer: str): #Returns individual status of programmer - finished, unfinished, workloads finished and unfinished

        if programmer not in self.programmers(): #Check if programmer exist, raise valueerror if not
            raise ValueError("Programmer not found!")
            
        
        #Using list comprehension to sum all tasks and hours
        finished = [order for order in self.__orders if order.programmer == programmer and order.is_finished()]
        unfinished = [order for order in self.__orders if order.programmer == programmer and not order.is_finished()]
        
        workload_finished = sum(int(order.workload) for order in finished)
        workload_unfinished = sum(int(order.workload) for order in unfinished)

        return (len(finished), len(unfinished), workload_finished, workload_unfinished)

        # The same but withour list comprehension

        #for order in self.orders:
        #    if order.is_finished() == True and order.programmer == programmer:
        #        finished += 1
        #        workload_finished += order.workload
        #    elif order.is_finished() == False and order.programmer == programmer:
        #        unfinished += 1
        #        workload_unfinished += order.workload


        #return (finished, unfinished, workload_finished, workload_unfinished)
        

class OrderBookAplication: #Main application

    def __init__(self) -> None:
        self.__orderbook = OrderBook()


    def help_menu(self): #User menu
        print("commands:"
              "\n0 exit"
              "\n1 add order"
              "\n2 list finished tasks"
              "\n3 list unfinished tasks"
              "\n4 mark task as finished"
              "\n5 programmers"
              "\n6 status of programmer")
        
    def add_order(self):
        description = input("description: ")
        programmer_and_estimate = input("programmer and workload estimate: ")

        #Split input and check if estimate is digit
        try:
            programmer = programmer_and_estimate.split(" ")[0]
            workload = programmer_and_estimate.split(" ")[1]
            
            if workload.isdigit() == False: #Return if is not digit
                print("erroneous input")
                return

            self.__orderbook.add_order(description, programmer, workload)
            print("added!")
        except:
             print("erroneous input") #Return if no hours input

    
    def finished_tasks(self): #
        finished =  self.__orderbook.finished_orders() #Returns finished tasks

        if len(finished) == 0: #If len 0 no finished tasks, return to menu
            print("no finished tasks")
            return
        
        for task in finished: #Print all finished tasks
            print(task)

    def unfinished_tasks(self): #Same like finished tasks
        unfinished =  self.__orderbook.unfinished_orders()
        
        for task in unfinished:
            print(task)
    
    def mark_finished(self): #Mark task as finished
        id = input("id: ")

        if id.isdigit() == False or int(id) >= 100:
            print("erroneous input")
            return
        else:
            self.__orderbook.mark_finished(int(id))
            print("marked as finished")
            
    
    def programmers(self): #Return all programmers
        programmers = self.__orderbook.programmers()

        for programmer in programmers:
            print(programmer)
    
    def programmers_status(self): #Returns individual programmer status
        programmer = input("programmer: ")

        if not programmer in self.__orderbook.programmers():
             print("erroneous input")
             return
        
        tasks = self.__orderbook.status_of_programmer(programmer)

        print(f"tasks: finished {tasks[0]} not finished {tasks[1]}, hours: done {tasks[2]} scheduled {tasks[3]}")
        
    
    def execute(self): 
        self.help_menu()
        while True:
            print("")
            command = input("command: ")

            if command == '0':
                break
            elif command == '1':
                self.add_order()
            elif command == '2':
                self.finished_tasks()
            elif command == '3':
                self.unfinished_tasks()
            elif command == '4':
                self.mark_finished()
            elif command == '5':
                self.programmers()
            elif command == '6':
                self.programmers_status()



apllication = OrderBookAplication()
apllication.execute()
