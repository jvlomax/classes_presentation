# Private class attributes in python
class Book:
    def __init__(self, pages):
        self.pages = pages
        self.current_page = 1
        
    def turn_page(self):
        self.current_page += 1

if __name__ == "__main__":
    book = Book(20)
    book.turn_page()                                                    # Turn a page
    print("You are currently on page {}".format(book.current_page))     # Page 2
    for i in range(18):                                                 # Turn the next 18 pages
        book.turn_page()
    
    print("You are currently on page {}".format(book.current_page))     # We should now be on the last page
    book.current_page += 1                                              # Access the current page directly
    
    print("Book has {} pages, you are currently on page {}".format(book.pages, book.current_page))  # We are now a page to far
