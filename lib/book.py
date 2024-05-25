#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.set_page_count(page_count)

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    page_count = property(get_page_count, set_page_count)
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

if __name__ == "__main__":
    book1 = Book("1984", 328)
    print(f"Book title: {book1.title}, Page count: {book1.page_count}")
    
    book2 = Book("Brave New World", "two hundred")  # This will trigger the error message
    print(f"Book title: {book2.title}, Page count: {book2.page_count if hasattr(book2, '_page_count') else 'N/A'}")
