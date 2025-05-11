from datetime import datetime

current_datetime = datetime.now()
current_time_string = current_datetime.strftime("%H:%M:%S")

# Parent class/ Super Class
class Item():
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability

    def borrow(cls):
        if cls.availability:
            cls.availability = False
            # print(f'The {cls.name} is not available')
            return f'The {cls.name} is not available'

    def returning(cls):
        if cls.availability:
            cls.availability = True
            # print(f'Thanks for retruning the {cls.name}')
            return f'Thanks for retruning the {cls.name}'
        

# Child Class/ Derived Class
class Book(Item):
    def __init__(self, name, availability, type, author):
        super().__init__(name, availability)
        self.author = author

        # Parent class attr wont be initialized as self.something in child class
        self.type = type
        self.author = author

    def display_info(self):
        return f'Book Info {self.name}, {self.author}'

book_1 = Book('Urdu Book', True, 'Learning', 'Ahmed Faraz')
print('Inherit', book_1.name)
print('Inherit', book_1.borrow())

print(book_1.display_info())


class DVD(Item):
    def __init__(self, name, availability, producer):
        super().__init__(name, availability)
        self.producer = producer

    def display_info(self):
        return f'DVD Info {self.name}, {self.producer}'


dvd1 = DVD('My DVD', True, 'Sami')
print(dvd1.producer)




print('=================================== Hospital Management System ===================================')


# Hospital Management System
class Paitent():
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def admit(self):
        return f'{self.name} is admitted to the hospital'
    
    def discharge(self):
        return f'{self.name} has been discharged'
    
class InPaitent(Paitent):
    def __init__(self, name, age, disease, room_number):
        super().__init__(name, age, disease)
        self.room_number = room_number

    def stay(self):
        return f'{self.name} is staying in the {self.room_number}'
    
p1 = InPaitent('Steve', 20, 'Heart Paitent', 202)
print(p1.name)
print(p1.stay())
print(p1.discharge())

class OutPaitent(Paitent):
    def __init__(self, name, age, disease, appointment_time):
        super().__init__(name, age, disease)
        self.appointment_time = appointment_time

    def visit(self):
        return f'{self.name} will be visting the hospital at {self.appointment_time}'
    
out_paitent = OutPaitent('Travis', 56, 'Blood Pressure', current_time_string)
print(out_paitent.appointment_time)