from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @abstractmethod
    def calculate_fine(self):
        pass

# Cannot make an instance of a ABC
person = Person() # Will producer an error    

class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

    # Implementing abstraction method
    def calculate_fine(self, days):
        return days * 2

member = Member('Ali' , 'ali@gmail.com' , 'mem-001')
print(member.mem_id)

# Calling the abstraction method
print("Fine On member",member.calculate_fine(10))


class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def get_info(self):
        return [self.name , self.salary]

    # Implementing abstraction method
    def calculate_fine(self, days):
        return self.salary - days


libraian = Librarian('Smith' , 'smith@gmail.com', 2393)

# Calling the abstraction method
print("Fine on librarian",libraian.calculate_fine(5))