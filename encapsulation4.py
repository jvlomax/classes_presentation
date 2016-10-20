class Book:
    def __init__(self, pages):
        self.pages = pages
        self.__current_page = 1                                 # We really don't want outsiders to access this attribute

    def turn_page(self):
        if self.__current_page < self.pages:
            self.__current_page += 1
        else:
            raise IndexError("There are no more pages in this book")

    def get_current_page(self):
        return self.__current_page

if __name__ == "__main__":
    book = Book(20)
    book.turn_page()
    print(book.__current_page)
    for i in range(18):
        book.turn_page()

    print("You are currently on page {}".format(book.get_current_page))
    try:
        book.turn_page()
    except IndexException:
        print("tried to read past the last page")

    book.__current_page += 1
    print("Book has {} pages, you are currently on page {}".format(book.pages, book._current_page))
