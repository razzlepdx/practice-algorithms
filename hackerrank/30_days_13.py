#Write MyBook class


class MyBook(Book):
    """ A class of books from an individual's library. """

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print "Title: {}".format(self.title)
        print "Author: {}".format(self.author)
        print "Price: {}".format(self.price)
