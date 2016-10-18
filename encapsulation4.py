class Book:
    def __init__(self, pages):
        self.pages = pages
        self.__current_page = 1 # This time we are serious. Just add more _
        
    def turn_page(self):
        if(self.__current_page < self.pages):
            self.__current_page += 1
        else:
            raise IndexError("There are no more pages in this book")
   
   
if __name__ == "__main__":
    book = Book(20)
    book.turn_page()
    print(book.__current_page)
    for i in range(18):
        book.turn_page()
    
    print("You are currently on page {}".format(book.__current_page))
    book.turn_page()
    
    print("Book has {} pages, you are currently on page {}".format(book.pages, book.__current_page))
   
    
    #book._current_page += 1
    #print("Book has {} pages, you are currently on page {}".format(book.pages, book._current_page))