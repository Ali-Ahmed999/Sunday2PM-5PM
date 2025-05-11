from datetime import datetime

current_datetime = datetime.now()
current_time_string = current_datetime.strftime("%H:%M:%S")

# Library Management System Ki encapculation ki example khud banani hai class main.

# Hospital Management System
class Paitent():
    def __init__(self, name, age, disease, amount):
        self.name = name
        self.age = age
        self.disease = disease
        self.__amount = amount

    def admit(self):
        return f'{self.name} is admitted to the hospital'
    
    def discharge(self):
        return f'{self.name} has been discharged'
    
    def get(self):
        return self.__amount

    def set(self, amount):
        return f'{self.name} has paid the {amount}'
    
class InPaitent(Paitent):
    def __init__(self, name, age, disease, amount, room_number ):
        super().__init__(name, age, disease, amount)
        self.room_number = room_number

    def stay(self):
        return f'{self.name} is staying in the {self.room_number}'
    
p1 = InPaitent('Steve', 20, 'Heart Paitent', 202, 1010101)
print(p1.name)
print(p1.stay())
print(p1.discharge())
print("In Paitent",p1.get())


class OutPaitent(Paitent):
    def __init__(self, name, age, disease, amount, appointment_time):
        super().__init__(name, age, disease, amount)
        self.appointment_time = appointment_time

    def visit(self):
        return f'{self.name} will be visting the hospital at {self.appointment_time}'


out_paitent2 = OutPaitent('Tim' , 12, 'Eye Infection',  2727112321313, current_datetime)
print("OUT PAITENT ==> ",out_paitent2.set(500))
print("OUT PAITENT GET ==> ",out_paitent2.get())