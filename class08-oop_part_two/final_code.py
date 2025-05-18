# final_output.py

from abc import ABC, abstractmethod

# Abstract Base Class - Person
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Abstract method that must be implemented by all subclasses
    @abstractmethod
    def calculate_fine(self, days):
        pass

    # Method to display info, can be overridden (polymorphism)
    def get_info(self):
        return f'{self.name}'


# Inheritance: Member and Librarian are subclasses of Person
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

    # Polymorphism: Overriding the get_info method in Member class
    def get_info(self):
        return { 'name': self.name, 'mem_id': self.mem_id }

    # Implementing the abstract method from Person class
    def calculate_fine(self, days):
        return days * 2


class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    # Polymorphism: Overriding the get_info method in Librarian class
    def get_info(self):
        return [self.name, self.salary]

    # Implementing the abstract method from Person class
    def calculate_fine(self, days):
        return self.salary - days


# Encapsulation: Library Class with private attribute __expenses
class Library():
    def __init__(self, name, location):
        self.lib_name = name
        self.lib_location = location
        # Private Attribute for expenses
        self.__expenses = {'salaryExp': 1232, 'KE_BILL': 1232}

    # Getter function to access private attribute
    def get_expenses(self):
        return self.__expenses
    
    # Setter function to update private attribute
    def update_expenses(self, update_exp):
        self.__expenses = update_exp
        return self.__expenses

    def add_book(self, new_book_name):
        return f'{new_book_name} has been added to the library.'

    def remove_book(self, remove_book):
        return f'{remove_book} has been removed from the library.'

    def get_books(self):
        return ["Book1", "Book2", "Book3"]


# --- Testing All the Concepts Together ---

# Creating instances of Member and Librarian
member = Member('Ali', 'ali@gmail.com', 'mem-001')
librarian = Librarian('Smith', 'smith@gmail.com', 2393)

# Using Polymorphism: calling get_info() for both Member and Librarian
print(member.get_info())  # Polymorphism: Member's version of get_info
print(librarian.get_info())  # Polymorphism: Librarian's version of get_info

# Encapsulation: Accessing and updating library expenses
library = Library('City Library', 'New York')
print(library.get_expenses())  # Encapsulation: Getter for private expenses
print(library.update_expenses({'salaryExp': 1500, 'KE_BILL': 1300}))  # Encapsulation: Setter to update expenses

# Abstraction: Calculating fine for Member and Librarian (abstract method implementation)
print(f"Fine for Member (Ali): {member.calculate_fine(5)}")
print(f"Fine for Librarian (Smith): {librarian.calculate_fine(5)}")

# Library actions (Adding and removing books)
print(library.add_book("New Book"))
print(library.remove_book("Book1"))
print(library.get_books())
