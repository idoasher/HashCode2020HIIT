class Library(object):
    def __init__(self, id, signup_time, scanning_throughput, books_ids):
        """
        :param id: id
        :param signup_time: {uint} time in days that it takes to sign the library up.
        :param scanning_throughput: {uint} The number of books that can be scanned each day.
        :param books: {list(uint)} ids of books in the library
        """
        self.id = id
        self.books_ids = books_ids
        self.signup_time = signup_time
        self.scanning_throughput = scanning_throughput
