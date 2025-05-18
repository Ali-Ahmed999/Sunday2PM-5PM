class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # Method defined here
    def get_info(self):
        return f'{self.name}'

class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

    # Same Parent Method. # Polymorphism starts here. 
    def get_info(self):
        return { 'name': self.name,'mem_id': self.mem_id}
    

member = Member('Ali' , 'ali@gmail.com' , 'mem-001')
print(member.mem_id)
print(member.get_info())

class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    # Same parent Method. # Polymorphism starts here. 
    def get_info(self):
        return [self.name , self.salary]

libraian = Librarian('Smith' , 'smith@gmail.com', 2393)
print(libraian.name)