class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Library():
    # constructor
    def __init__(self, name, location):
        # Class Attributes/ Class Variables/ Parameters
        self.lib_name = name
        self.lib_location = location
        # Declaring a Private Attribute
        self.__expenses = {'salaryExp':1232 , 'KE_BILL':1232}

    # getter function
    def get_expenses(self):
        return self.__expenses
    
    # Setter Function
    def update_expenses(self, update_exp):
        # self.__expenses = {'salaryExp':1232 , 
        #                    'KE_BILL':1232 , 
        #                    'furniture': 423423}
        self.__expenses = update_exp
        return self.__expenses

    # class methods/ functions
    def add_book(self, new_book_name):
        return self.books.append(new_book_name)

    def remove_book(self, remove_book):
        return self.books.remove(remove_book)

    def get_book(self):
        return self.books

# Making an Obj/ Creating instance of a class
mylib = Library('The library', 'Karachi')
print(mylib.get_expenses())
print(mylib.update_expenses(
        {'salaryExp':1232 , 'KE_BILL':1232 , 'furniture': 423423}
    ))