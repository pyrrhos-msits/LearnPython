class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    def __repr__(self):
        return'{} by {}. ${}. [{}]'.format(self.title, self.author, self.price, self.book_id)

# my_book = Book('Frank', 'Buchtitel', 15.99, '4711-0815')
# print(my_book)