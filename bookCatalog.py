class Book:

    def __init__(self,title,author,isbn,copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies
        #Book.books[isbn]=self
    def display(self):
        print(f"titlte:{self.title} \n author:{self.author}\n isbn no:{self.isbn} \n no of copies:{self.copies} ")   
class BookLibrary:
    def __init__(self):
        self.books=[]
                      
    def add_book(self,new_book):
        
        self.books.append(new_book)
        print(f"the newly book {new_book.title} is added")
    def remove_book(self,isbn):
        for i in self.books:
            if i.isbn == isbn:
                self.books.remove(i)
                print(f"book with isbn{i.isbn} is removed")
           
        print("no book was found")    
    def find_book(self,isbn):
        for j in self.books:
            if j.isbn == isbn:
                 print(f"book with isbn {isbn}was found")
                 j.display()
                 return j
                    
       
        print("there is no such book with isbn number") 
    def display_books(self):
        
        if not self.books:
            print("No books in the library.\n")
        else:
            print("Library Collection:\n")
            for book in self.books:
                book.display()       
lib=BookLibrary()   

ob=Book("rich dad poor dad","william",123456789,200) 
book2 = Book("Wings of Fire", "A.P.J. Abdul Kalam", 987654321, 150)
lib.add_book(ob)
lib.add_book(book2)
lib.display_books()
lib.find_book(123456789)
lib.remove_book(123456789)
lib.display_books()


#ob.remove_book()
#ob.find_book(123456789)      