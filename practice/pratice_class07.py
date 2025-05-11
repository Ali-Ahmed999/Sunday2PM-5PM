class Book():
    # __init__ is the first mandotary defined in every class. It is called when a class instance is created.
    # (self, this, cls) are the mandotary parameter defined in the methods created in class

    def __init__(self, name, author, availability):
        self.name = name
        self.author = author
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

# creating the instance of a class
book1 = Book('Physics book', 'John', True)
book2 = Book('Maths book', 'Ali Jawwad', True)
print(book1.name)
print(book1.borrow())
print(book1.returning())

class Library():
    def __init__(self):
        self.book = []

    def add_book(self, bookname):
        self.book.append(bookname)
        return f'{bookname} has been added to the library'


    def remove_book(self, removeBook):
        self.book.remove(removeBook)
        return f'{removeBook} has been removed'
        
    def list_book(self):
        return self.book


library = Library()
print('Adding a book to library <==> ',library.add_book(book1.name))
print('Adding a book to library <==> ',library.add_book(book2.name))
print(library.list_book())

print(library.remove_book('Science book'))
print(library.list_book())




