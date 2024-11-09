import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.

        test1 = BookLover('Mike', 'myemail@email.com', 'fiction')
        test1.add_book("Shutter Island",5)

        # get the book list, turn the book name column into a list, 
        # get the first element of that list, which should be the only book 
        self.assertTrue(list(test1.book_list['book_name'])[0] == "Shutter Island")

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.

        test2 = BookLover('Mike', 'myemail@email.com', 'fiction')
        test2.add_book("Shutter Island",5)
        test2.add_book("Shutter Island",5)

        # the number of books read should only be equal to 1
        self.assertEqual(test2.num_books_read(), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.

        test3 = BookLover('Mike', 'myemail@email.com', 'fiction')
        test3.add_book("Shutter Island",5)

        # using the has_read function to test if true
        self.assertTrue(test3.has_read("Shutter Island"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`

        test4 = BookLover('Mike', 'myemail@email.com', 'fiction')
        test4.add_book("Shutter Island",5)

        #using has_read function to test if false
        self.assertFalse(test4.has_read("Gateway"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.

        test5 = BookLover('Mike', 'myemail@email.com', 'fiction')
        test5.add_book("Shutter Island",5)
        test5.add_book("Love it",5)
        test5.add_book("17", 2)

        # using num_books_read to confirm 3 books are equal
        self.assertEqual(test5.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        # for this test I am summing up the booleans of the book ratings above 3, 
        #then comparing that to the number of books returned in favorites. 

        test6 = BookLover('Mike', 'myemail@email.com', 'fiction')
        test6.add_book("Shutter Island",5)
        test6.add_book("Love it",4)
        test6.add_book("17", 2)
        self.assertEqual(sum(test6.fav_books()['book_rating'] > 3), len(test6.fav_books()))
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
