class library :
    def __init__(self) :
       self.no_of_books = 0
       self.books =  [ ]
    def info (self) :
        print(f"there are total  {self.no_of_books} books and these are : {self.books} " )

    def add_books (self , newbooks ) :
        self.books.append(newbooks)
        self.no_of_books=self.no_of_books+1
        

e1 = library ()
e1.add_books ("piyush")
e1.info ()

e2 = library ()
e2.add_books ("pihu")
e2.info ()