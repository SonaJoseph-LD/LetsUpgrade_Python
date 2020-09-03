class Library():
    def __init__(self, list_of_book, library_name):
        self.lend_data = {}
        self.list_of_book = list_of_book
        self.library_name = library_name


        for book in self.list_of_book:
            self.lend_data[book] = None

    def display_book(self):
        for index, book in enumerate(self.list_of_book):
            print(f"{index}) {book}")

    def lend_book(self, book_name, lender):
        self.book_name = book_name
        self.lender = lender
        if book_name in self.list_of_book:
            if self.lend_data[book_name] is None:
                self.lend_data[book_name] = self.lender
                print("Lend Done")
            else:
                print(f"The book is lended to {self.lend_data[book_name]}")

        else:
            print("Please Enter the valid book name")

    def add_book(self, addbk):
        self.addbk = addbk
        self.list_of_book.append(self.addbk)

    def return_book(self, returnbk):
        self.returnbk = returnbk
        if returnbk in self.list_of_book:
            if self.lend_data[returnbk] is not None:
                self.lend_data[returnbk] = None
            else:
                print("This book was not lended")
        else:
            print("Enter correct book name")

if __name__ == '__main__':
    list_of_book = ['C++', 'Object oriented', 'Computer app', 'JavaScript']
    library_name = "Sona's Library"
    SonaLibrary = Library(list_of_book, library_name)

    while True:


        opt = int(input("Enter Any one Option \n\n"
                        "1) Display Books\n"
                        "2) Lend Book\n"
                        "3) Add Book\n"
                        "4) Return Book\n\n"))
        if opt == 1:
            print(SonaLibrary.display_book())

        elif opt == 2:
            lender = input("Enter your name :\n")
            book_name = input("Enter the Book Name :\n")
            SonaLibrary.lend_book(book_name, lender)
        elif opt == 3:
            addbk = input("Enter the book to be added :\n")
            SonaLibrary.add_book(addbk)
        elif opt == 4:
            returnbk = input("Which book you have to return ? \n")
            SonaLibrary.return_book(returnbk)
        else:
            print("sorry")









