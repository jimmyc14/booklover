import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[],'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False

    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        filtered = self.book_list[self.book_list['book_rating'] > 3]
        return filtered

if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("War of the Worlds 2", 5)
    test_object.add_book("War of the Worlds 3", 1)
    
    # print(test_object.name)
    # print(test_object.email)
    # print(test_object.fav_genre)
    # print(test_object.num_books)
    # print(test_object.book_list)
    # print(test_object.has_read("War of the Worlds"))
    # print(test_object.num_books_read())
    # print(test_object.fav_books())

    print(test_object.fav_books()['book_rating']>3)