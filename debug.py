import ipdb;

from lib.many_to_many import *

king = Author("King")

shining = Book("the shining")

big = king.sign_contract(shining, "0514985", 10000 )

author = Author("Name")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
    
Contract(author, book1, "01/01/2001", 10)
Contract(author, book2, "01/01/2001", 20)
Contract(author, book3, "01/01/2001", 30)

ipdb.set_trace()