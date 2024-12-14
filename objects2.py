class Employee:

    #Initializing (Constructor)
    def __init__(self):
        print('Employee created.')

    #Deleting (Destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj

class library:

    def __init__(self,list_of_books, name):
        self.booklist = list_of_books
        self.name = name
        self.lendict = {}

    def displayBooks(self):
        print("We have the following books:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.booklist:
            print("Sorry,we don't have that book.")
        elif book in self.lendict:
            print(f"The book is already being used by{self.lendict[book]}")
        else:
            self.lendict[book] = user
            print(
                   "Lender-Book database has been updated. You can take the book now."
            )

        def addbook(self,book):
            self.booklist.append(book)
            print(f"{book} has been added to the book list.")

        def returnbook(self,book):
            if book in self.lendict:
                del self.lendict[book]
                print("Book has been returned.")
            else:
                print("That book wasn't borrowed from us.")

    
