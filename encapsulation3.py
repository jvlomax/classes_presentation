class Book:
    def __init__(self, pages):
        self.pages = pages
        self._current_page = 1                                  # This is now marked as private
        
    def turn_page(self):
        if(self._current_page < self.pages):                    # Before we turn the page, we make sure there are more pages
            self._current_page += 1
        else:
            raise IndexError("There are no more pages in this book")
   
   
if __name__ == "__main__":
    book = Book(20)
    book.turn_page()
    print("You are currently on page {}".format(book._current_page))
    for i in range(18):
        book.turn_page()
    
    print("You are currently on page {}".format(book._current_page))                # We are now on the last page
    try:
        book.turn_page()                                                                # We should not be able to change the page
    except IndexError:
        print("we tried to turn past the last page")

    

    #book._current_page += 1                                                         # But we can still access it if we really want
    #print("Book has {} pages, you are currently on page {}".format(book.pages, book._current_page))
