class book:
    def __init__(self,author,title):
        self.author=author
        self.title=title
        self.is_available=True
    def __str__(self):
        return f'{self.title} by {self.author}-{'Available' if self.available=True else 'Not Avaiable'}

class library(self):
    self.books=[]

    def add_book(self,author,title):
        new_book=book(author,title)
        self.books.append(new_book)

    def display_book(self):
        if not self.books:
            print("Books are not Available")
        else:
            for idx,books in enumerate(self.books,start=1):
                print(f'{idx}.{books}')

    def borrow_book(self,index):
        if (0<index<len(self.books)):
            book=self.books[index-1]
            if book.is_available:
                book.is_available=False
                print(f'You have successfully borrowed the book - {book}')
            else:
                print("This book is already borrowed and not returned yet!")
            
        else:
            print("Please enter the correct book number!")

    def return_book(self,index):
        if (0<index<len(index-1)):
            returned_book=self.books[index-1]
            if not returned_book.is_available:
                returned_book.is_available=True
                print(f'You have successfully returned the book - {returned_book}')
            else:
                print("This book is not borrowed")
        else:
            print("Please enter the correct book number")

def main():
    library=library()

    while True:
        print("---- Library Menu ----\n")
        print("1.Add book")
        print("2.Display books")
        print("3.Borrow book")
        print("4.Return book")
        print("5.Exit")
