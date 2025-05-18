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


# Making an Obj/ Creating instance of a class
# mylib = Library('The library', 'Karachi')
# print(mylib.lib_name)
# print(mylib.lib_location)




class Book():
    def __init__(self, name, author, availability):
        self.book_name = name
        self.author_name = author
        self.availability = availability

    def borrow(self):
        self.availability
    



# Instance of class
book1 = Book('Poetry', 'Allama iqbal', True)
print(book1.book_name)
print(book1.author_name)
print(book1.availability)


book2 = Book('Comedy', 'Umer Sharif', True)
book3 = Book('Tragedy', 'Ahemd', True)

mylib2 = Library('The library', 'Karachi')
# Adding books to the list (In library)
print(mylib2.add_book(book2.book_name))
print(mylib2.add_book(book3.book_name))

# Getting the list of books (In Library)
print(mylib2.get_book())

# Removing the book (In Library)
print(mylib2.remove_book('Tragedy'))

# Fetching the list again after removing
print(mylib2.get_book())