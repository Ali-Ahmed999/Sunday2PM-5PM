class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def walk(self):
        print('Walking')

# Inheritance starts here
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

member = Member('Ali' , 'ali@gmail.com' , 'mem-001')
print(member.mem_id)
print(member.walk())

class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary
                
libraian = Librarian('Smith' , 'smith@gmail.com', 2393)
print(libraian.name)


class Library():
    # constructor
    def __init__(self, name, location):
        # Class Attributes/ Class Variables/ Parameters
        self.books = []
        self.lib_name = name
        self.lib_location = location

    # class methods/ functions
    def add_book(self, new_book_name):
        return self.books.append(new_book_name)

    def remove_book(self, remove_book):
        return self.books.remove(remove_book)

    def get_book(self):
        return self.books


class Book():
    def __init__(self, name, author, availability):
        self.book_name = name
        self.author_name = author
        self.availability = availability

    def borrow(self):
        self.availability
    

# Instance of class
# book1 = Book('Poetry', 'Allama iqbal', True)
# print(book1.book_name)
# print(book1.author_name)
# print(book1.availability)


# book2 = Book('Comedy', 'Umer Sharif', True)
# book3 = Book('Tragedy', 'Ahemd', True)

# mylib2 = Library('The library', 'Karachi')
# # Adding books to the list (In library)
# print(mylib2.add_book(book2.book_name))
# print(mylib2.add_book(book3.book_name))

# # Getting the list of books (In Library)
# print(mylib2.get_book())

# # Removing the book (In Library)
# print(mylib2.remove_book('Tragedy'))

# # Fetching the list again after removing
# print(mylib2.get_book())