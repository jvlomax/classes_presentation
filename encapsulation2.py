class Book:
    def __init__(self, pages):
        self.pages = pages
        self.current_page = 1
        
    def turn_page(self):
        self.current_page += 1
        
   
   
if __name__ == "__main__":
    book = Book(20)
    book.turn_page()
    print(book.current_page)
    for i in range(18):
        book.turn_page()
    
    print("You are currently on page {}".format(book.current_page))
    book.current_page += 1
    
    print("Book has {} pages, you are currently on page {}".format(book.pages, book.current_page))
      