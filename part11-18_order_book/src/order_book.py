class Task:

    program_id = 0
    def __init__(self, description: str, programmer: str, workload: int):
        
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.program_status = False
        Task.program_id += 1
        self.id = Task.program_id

        
    def id(self):
        
        return self.id

    def mark_finished(self):
        self.program_status = True


    def is_finished(self):
        return self.program_status
    
    
    def __str__(self) -> str:

        program_end = 'FINISHED'if self.program_status == True else 'NOT FINISHED'

        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {program_end}"
    
class OrderBook:

    def __init__(self):
        self.orders = []
        

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.orders.append(order)

    def all_orders(self):
        return [order for order in self.orders]
    
    def programmers(self):
          return list(set([order.programmer for order in self.orders]))
    
    def mark_finished(self, id: int):

        id_found = False

        for order in self.orders:
            if order.id == id:
                id_found = True

        if id_found == False:
            raise ValueError(f"Order with {id} not found")

        return [order.mark_finished() for order in self.orders if order.id == id]

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished() == True]

    def unfinished_orders(self):
        return [order for order in self.orders if order.is_finished() == False]
    
    def status_of_programmer(self, programmer: str):

        if programmer not in self.programmers(): #Check if programmer exist, raise valueerror if not
            raise ValueError("Programmer not found!")
        
        #Using list comprehension to sum all tasks and hours
        finished = [order for order in self.orders if order.programmer == programmer and order.is_finished()]
        unfinished = [order for order in self.orders if order.programmer == programmer and not order.is_finished()]
        
        workload_finished = sum(order.workload for order in finished)
        workload_unfinished = sum(order.workload for order in unfinished)

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
        


if __name__ == "__main__":
    
   t = Task("code hello world", "Andy", 3)
   print(t)
